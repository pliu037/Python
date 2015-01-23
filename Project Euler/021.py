#https://projecteuler.net/problem=21

from tools import findPrimes
from tools import findDivisors
from gmpy2 import isqrt

'''
'''
def isAmicable(n):
    return 0

'''
'''
def findSumAmicable(n):
    primesArray = findPrimes(isqrt(n))
    sums = []
    for i in xrange(1, n):
        sums.append(sum(findDivisors(primesArray, i)))
    return sorted(sums)
    
print findSumAmicable(100)