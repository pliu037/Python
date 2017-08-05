"""
README
I went with a hybrid encoding strategy. The method performs lossless compression by representing runs of repeating
characters as a pair of chrs, character and count (count is converted to a chr). This function is 1 to 1 with the run
it represented and so can be converted back losslessly. This method provides good compression in the case of many or
large runs of repeating characters. The hybrid part comes in for strings without many or long runs of repeating
characters. If the compressed string is longer than the original, then the original string is used.

The data file should be named '2017 - plaid - data.txt' or one can just change the file path in test_encode_decodable.
"""

import unittest


class Encoder:
    def encode(self, string):
        """
        Given a string, returns the losslessly encoded string.
        Compresses the string by aggregating repeating, consecutive characters into (character, count) pairs where the
        count is stored as a chr in the output string. Since chr only goes up to 255, if <count> is greater than 255,
        multiple (character, count') pairs are emitted (the sum of the <count'>s should add up to <count>).
        If the compressed string is larger than the original string (i.e.: when there are few runs of repeating
        characters), returns the original string.
        Prepends 'c' if using the compressed string and 'o' if using the original string.
        :param string: str
        :return: str
        """
        if not string:
            return ''

        output = []
        last_char = string[0]
        last_count = 1
        for c in string[1:]:
            if c != last_char:
                tup = (last_char, last_count)
                output.append(tup)
                last_char = c
                last_count = 1
            else:
                last_count += 1
        tup = (last_char, last_count)
        output.append(tup)
        ret = ''.join(Encoder.encode_tuple(tup) for tup in output)
        if len(ret) < len(string):
            return 'c' + ret
        return 'o' + string

    def decode(self, string):
        """
        Given an encoded string, returns the decoded string.
        See encode for a description of how a string is encoded, which should elucidate how decoding works.
        Raises RuntimeErrors if the string is malformed (i.e.: invalid leading chr, character with no matching count)
        :param string: str
        :return: str
        """
        if not string:
            return ''

        if string[0] == 'o':
            return string[1:]
        elif string[0] == 'c':
            string = string[1:]
        else:
            raise RuntimeError('Encoded data corrupted')

        if len(string) % 2 != 0:
            raise RuntimeError('Encoded data corrupted')

        output = []
        for i in xrange(len(string)/2):
            tup = (string[2*i], string[2*i + 1])
            output.append(tup)
        return ''.join([Encoder.decode_tuple(tup) for tup in output])

    @staticmethod
    def encode_tuple(tup):
        """
        Given a tuple of (character, count), returns the string that encodes the given tuple (i.e.: converts <count> to
        a chr). Since chr only goes up to 255, if <count> is greater than 255, multiple (character, count') pairs are
        emitted (the sum of the <count'>s should add up to <count>).
        :param tup: (character, count [in int form])
        :return: str
        """
        ret = ''
        count = tup[1]
        while count > 255:
            ret += ''.join([tup[0], chr(255)])
            count -= 255
        return ret + ''.join([tup[0], chr(count)])

    @staticmethod
    def decode_tuple(tup):
        """
        Given a tuple (character, count [in chr form]), converts <count> to int form and emits a string of length
        <count> made up entirely of <character>.
        :param tup: (character, count [in chr form])
        :return: str
        """
        return tup[0]*ord(tup[1])


class TestEncoder(unittest.TestCase):
    def test_encode_empty_string(self):
        encoder = Encoder()
        self.assertEqual(encoder.encode(''), '')

    def test_decode_empty_string(self):
        encoder = Encoder()
        self.assertEqual(encoder.decode(''), '')
        self.assertEqual(encoder.decode('c'), '')
        self.assertEqual(encoder.decode('o'), '')

    def test_decode_invalid_string(self):
        encoder = Encoder()
        with self.assertRaises(RuntimeError):
            encoder.decode('bad')
        with self.assertRaises(RuntimeError):
            encoder.decode('ca')

    def test_encode_correct(self):
        encoder = Encoder()
        self.assertEqual(encoder.encode('aaaaabbbcccc'), ''.join(['c', 'a', chr(5), 'b', chr(3), 'c', chr(4)]))
        self.assertEqual(encoder.encode('abcdefg'), 'oabcdefg')

    def test_decode_correct(self):
        encoder = Encoder()
        self.assertEqual(encoder.decode('oabcdefg'), 'abcdefg')
        self.assertEqual(encoder.decode(''.join(['c', 'a', chr(3), 'b', chr(7), 'c', chr(2)])), 'aaabbbbbbbcc')

    def test_encode_decodable(self):
        encoder = Encoder()
        file_data = TestEncoder.get_file_data('./2017 - plaid - data.txt')
        self.assertTrue(TestEncoder.compare_equals(encoder.decode(encoder.encode(file_data)), file_data))

    @staticmethod
    def compare_equals(string1, string2):
        if len(string1) != len(string2):
            return False
        for tup in zip(string1, string2):
            if tup[0] != tup[1]:
                return False
        return True

    @staticmethod
    def get_file_data(file_name):
        with open(file_name, 'r') as f:
            return f.read()


if __name__ == '__main__':
    unittest.main()
