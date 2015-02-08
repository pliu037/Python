#https://projecteuler.net/problem=27

from tools import findPrimes
from tools import checkPrime

#Returns the value of a*x**2 + b*x + c
def quadraticExpression (b, c, x):
    return x**2 + b*x + c

'''
Finds b and c such that f(x) = x**2 + bx + c generates the longest sequence of primes starting from
x = 0, where |b|, |c| < n, and returns the product bc
Method:
Since f(0) must be prime to start a sequence of primes, only prime values of c are checked.
'''
def findLongestPrimeChain(n):
    longestChain = 0
    longestProduct = 0
    primesArray = findPrimes(n)
    for prime in primesArray:
        for b in xrange(n):
            count = 1
            while checkPrime(primesArray, quadraticExpression(b, prime, count)):
                count += 1
            if count > longestChain:
                longestChain = count
                longestProduct = prime*b
            count = 1
            while quadraticExpression(-b, prime, count) > 0 and \
                  checkPrime(primesArray, quadraticExpression(-b, prime, count)):
                count += 1
            if count > longestChain:
                longestChain = count
                longestProduct = prime*(-b)
    return longestProduct

print findLongestPrimeChain(1000)