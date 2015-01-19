#https://projecteuler.net/problem=24

from itertools import permutations

'''
Finds and returns the n-th lexographic permutation of strng
Method:

'''
def myLexographicPermutation(strng, n):
    elements = sorted(strng)
    return elements
    
#Finds and returns the n-th lexographic permutation of strng
def lexographicPermutation(strng, n):
    iterator = permutations(sorted(strng), len(strng))
    for _i in xrange(n - 1):
        iterator.next()
    return iterator.next()
    
print lexographicPermutation('0123456789', 1000000)
print myLexographicPermutation('0123456789', 1000000)