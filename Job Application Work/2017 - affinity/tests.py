from date_parser import Date
from score_parser import Score
import unittest


class Tests(unittest.TestCase):
    def test_date_parser_correct_input(self):
        self.assertEqual(Date('Feb 28, 1987').output_string(), 'Feb 28, 1987')
        self.assertEqual(Date('2/28/1987').output_string(), 'Feb 28, 1987')
        self.assertEqual(Date('February 28, 1987').output_string(), 'Feb 28, 1987')
        self.assertEqual(Date('2/29/2000').output_string(), 'Feb 29, 2000')

    def test_date_parser_incorrect_input(self):
        with self.assertRaises(RuntimeError):
            Date('Febr 28, 1987')
        with self.assertRaises(RuntimeError):
            Date('13/28/1987')
        with self.assertRaises(RuntimeError):
            Date('0/28/1987')
        with self.assertRaises(RuntimeError):
            Date('a/2a/198a')
        with self.assertRaises(RuntimeError):
            Date('2/29/1999')

    def test_score_parser_correct_input(self):
        self.assertEqual(Score('5000000').output_string(), '"5,000,000"')
        self.assertEqual(Score('5,000,000').output_string(), '"5,000,000"')
        self.assertEqual(Score('5000k').output_string(), '"5,000,000"')
        self.assertEqual(Score('5M').output_string(), '"5,000,000"')

    def test_score_parser_incorrect_input(self):
        with self.assertRaises(RuntimeError):
            Score('a500,000')
        with self.assertRaises(RuntimeError):
            Score('500a000')
        with self.assertRaises(RuntimeError):
            Score('5000a')


if __name__ == '__main__':
    unittest.main()
