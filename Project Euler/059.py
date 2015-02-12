#https://projecteuler.net/problem=59

from tools import get2DData
from itertools import permutations

#XORs two chars (in int representation) and returns the result in char representation
def xor(a,b):
    return chr(a^b)

'''
Finds and returns, for each unit in strng, the number of encoded characters yielding a common
character when XORed with the given unit
Observation:
Assuming the positions of any given character in the decoded message are near-uniformly distributed
modulo the length of the key, higher counts of decoding an encoded character into a common character
correlate with a unit's probability of being present in the key. Though this method does not find
the key, it prioritizes which permutations to try first.
'''
def findHint(encoded, strng):

    '''
    The set of what is defined as a "common" characters. The greater the average occurrence of the
    "common" characters, the greater the resolving power of this method.
    '''
    commonCharacters = set(" ")

    frequencies = [0 for _i in xrange(len(strng))]
    for i in xrange(len(strng)):
        count = 0
        for letter in encoded:
            if xor(letter, ord(strng[i])) in commonCharacters:
                count += 1
        frequencies[i] = count
    return frequencies

'''
Finds and returns the sum of the int representations of all of the characters of the decoded string
given that the key is known to be of length n and consisting only of characters in strng
'''
def findSumDecoded(encoded, n, strng):

    '''
    The set of what is defined as a "common" words. The greater the average occurrence of the
    "common" words, the greater the resolving power of this method.
    '''
    commonWords = ["the"]

    iter = permutations(strng, n)
    maxCount = 0
    maxDecoded = ""
    for check in iter:
        decoded = ""
        i = 0
        for letter in encoded:
            decoded += xor(ord(check[i]), letter)
            i += 1
            i %= n
        for word in commonWords:
            count = decoded.count(word)
        if count > maxCount:
            maxCount = count
            maxDecoded = decoded
    count = 0
    for char in maxDecoded:
        count += ord(char)
    return count

print findHint(get2DData()[0], "abcdefghijklmnopqrstuvwxyz")
print findSumDecoded(get2DData()[0], 3, "abcdefghijklmnopqrstuvwxyz")