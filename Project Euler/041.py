#https://projecteuler.net/problem=41

from itertools import permutations
from tools import findPrimes
from tools import checkPrime
from gmpy2 import isqrt

'''
Finds and the returns the largest up-to-n pandigital prime (an n-pandigital number contains each digit
from 1 to n once) prime
Method:
Tests decreasing permutations of the digits 1 through i, starting with i = n through i = 1, for
primality.
'''
def findLargestPandigitalPrime(n):
    primesArray = findPrimes(isqrt(10**n))
    for i in xrange(n):
        digits = []
        for j in xrange(1, n + 1 - i):
            digits.append(j)
        digits.reverse()
        permIter = permutations(digits, n - i)
        for check in permIter:
            if checkPrime(primesArray, int(''.join(str(k) for k in check))):
                return check
    
print findLargestPandigitalPrime(9)