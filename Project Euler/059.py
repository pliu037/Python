#https://projecteuler.net/problem=59

from tools import get2DData
from itertools import permutations

#XORs two chars (in int representation) and returns the result in char representation
def xor(a,b):
    return chr(a^b)

'''
Finds and returns, for each character in strng, the number of encoded letters yielding a common
character when XORed with the given character
Observation:

'''
def findHint(encoded, strng):
    commonCharacters = set(" eE")
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
Method:

'''
def findKey(encoded, n, strng):
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
        count = decoded.count("the")
        if count > maxCount:
            maxCount = count
            maxDecoded = decoded
    count = 0
    for char in maxDecoded:
        count += ord(char)
    return count

print findHint(get2DData()[0], "abcdefghijklmnopqrstuvwxyz")
print findKey(get2DData()[0], 3, "abcdefghijklmnopqrstuvwxyz")