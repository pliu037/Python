#https://projecteuler.net/problem=23

from itertools import combinations_with_replacement
from tools import findPrimes
from tools import findDivisors

'''
Given an array of primes up to n, determines if n is an abundant number (a number for which the sum of
its proper divisors is greater than itself) and returns True if it is
'''
def isAbundant(primesArray, n):
    divisors = findDivisors(primesArray, n)
    if (sum(divisors) > n):
        return True
    return False

#Finds abundant numbers between 1 and maxCheck, exclusive, and returns them as an array
def getAbundantNumbers(maxCheck):
    primesArray = findPrimes(maxCheck)
    abundantNumbers = []
    for i in xrange(1, maxCheck):
        if isAbundant(primesArray, i):
            abundantNumbers.append(i)
    return abundantNumbers

'''
Finds and returns the sum of all positive integers that cannot be written as the sum of two abundant
numbers
Method:
Generates a set of the sum of any two abundant numbers. Since any integer larger than 28123 can be
expressed as the sum of two abundant numbers, only abundant numbers less than 28124 matter.
'''
def getSumNonSumOfAbundantNumbers():
    MAX_CHECK = 28123 + 1
    abundantNumbers = getAbundantNumbers(MAX_CHECK)
    
    #Uses a set to remove duplicate sums
    sumOfAbundantNumbers = set()
    comboIters = combinations_with_replacement(abundantNumbers, 2)
    for i in comboIters:
        sumOfAbundantNumbers.add(sum(i))
        
    currentSum = 0
    for i in xrange(1, MAX_CHECK):
        if i not in sumOfAbundantNumbers:
            currentSum += i
    return currentSum
    
print getSumNonSumOfAbundantNumbers()