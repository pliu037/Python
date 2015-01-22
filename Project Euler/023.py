#https://projecteuler.net/problem=23

from gmpy2 import isqrt
from itertools import combinations
from itertools import combinations_with_replacement
from tools import findPrimes

'''
Given an array of primes up to isqrt(n) (this condition is enforced by getAbundantNumbers), finds the
prime factors of n and returns them as an array
'''
def findPrimeFactors(primesArray, n):
    primeFactors = []
    for i in primesArray:
        while (n % i == 0):
            n = n / i
            primeFactors.append(i)
        if n == 1:
            break
    return primeFactors

#Given an array of prime factors, finds the proper divisors and returns them as an array
def findDivisors(primeFactors):
    
    #Uses a set to remove duplicate products
    divisorPrimeFactors = set()
    for i in xrange(1, len(primeFactors)):
        comboIter = combinations(primeFactors, i)
        for j in comboIter:
            divisorPrimeFactors.add(j)
            
    divisors = [1]
    for i in divisorPrimeFactors:
        currentProduct = 1
        for j in i:
            currentProduct *= j
        divisors.append(currentProduct)
    return divisors

'''
Given an array of primes up to isqrt(n) (this condition is enforced by getAbundantNumbers), determine
if n is an abundant number (a number for which the sum of its proper divisors is greater than itself)
and returns True if it is
'''
def isAbundant(primesArray, n):
    primeFactors = findPrimeFactors(primesArray, n)
    divisors = findDivisors(primeFactors)
    if (sum(divisors) > n):
        return True
    return False

#Finds abundant numbers between 1 and maxCheck and returns them as an array
def getAbundantNumbers(maxCheck):
    primesArray = findPrimes(isqrt(maxCheck))
    abundantNumbers = []
    for i in xrange(1, maxCheck):
        if isAbundant(primesArray, i):
            abundantNumbers.append(i)
    return abundantNumbers

'''
'''
def getSumNonSumOfAbundantNumbers():
    MAX_CHECK = 28124
    abundantNumbers = getAbundantNumbers(MAX_CHECK)
    
    #Uses a set to remove duplicate sums
    sumOfAbundantNumbers = set()
    comboIters = combinations_with_replacement(abundantNumbers, 2)
    for i in comboIters:
        sumOfAbundantNumbers.add(sum(i))
        
    currentSum = 0
    for i in xrange(1, MAX_CHECK):
        if i not in sumOfAbundantNumbers:
            print i
            currentSum += i
    return currentSum
    
print getSumNonSumOfAbundantNumbers()