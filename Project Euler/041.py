#https://projecteuler.net/problem=41

from itertools import permutations
from tools import findPrimes
from gmpy2 import isqrt

#Given an array of primes up to at least sqrt(n), returns True if n is prime
def checkPrime(primesArray, n):
    for i in primesArray:
        if (n % i == 0) and (i < isqrt(n)):
            return False
    return True

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