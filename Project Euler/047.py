#https://projecteuler.net/problem=47

from tools import findPrimeFactors
from tools import findPrimes

'''
Finds and returns the lowest member of n consecutive integers such that each integer is composed of
n distinct primes (p**i counts as one distinct prime, p)
'''
def findConsecNUniquePrimeFactors(n):
    primesArray = findPrimes(10**n)
    distinctPrimeFactors = []

    #Start from the smallest integer that is composed of n distinct primes
    i = 1
    for j in xrange(n):
        i *= primesArray[j]

    while True:

        #Use set to eliminate duplicate prime factors
        distinctPrimeFactors.append(len(set(findPrimeFactors(primesArray, i))))

        length = len(distinctPrimeFactors)
        if (length >= n and distinctPrimeFactors[length - 1] == n):
            flag = True
            for j in xrange(1, n):
                if distinctPrimeFactors[length - j - 1] != n:
                    flag = False
                    break
            if flag:
                return i - n + 1
        i += 1

print findConsecNUniquePrimeFactors(4)