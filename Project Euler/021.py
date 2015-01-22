#https://projecteuler.net/problem=21

from gmpy2 import isqrt
from itertools import combinations
from tools import findPrimes

'''
'''
def primeFactors(n):
    return 0

'''
'''
def isAmicable(n):
    return 0

'''
'''
def findSumAmicable(n):
    primes = findPrimes(isqrt(n))
    print primes
    
print findSumAmicable(10000)