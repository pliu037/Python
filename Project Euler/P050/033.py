#https://projecteuler.net/problem=33

from tools import findPrimes
from gmpy2 import isqrt

'''
Determines if x and y are cancellable (removing the same digit from x and y yields x' and y' such that
x/y = x'/y' and returns True if it is
Method:
Removing the same digit from the same position from both x and y is equivalent to subtracting a
constant from both (x' = x - c and y' = y - c). Given x != y, it is impossible that x/y = x'/y'.
'''
def isCancellable(x, y):
    if ((x / 10) == (y % 10)):
        xPrime = x % 10
        yPrime = y / 10
        if (xPrime*y == yPrime*x):
            return True
    if ((x % 10) == (y / 10)):
        xPrime = x / 10
        yPrime = y % 10
        if (xPrime*y == yPrime*x):
            return True
    return False

'''
Given an array of primes up to sqrt(max(x, y)), removes all common factors from both x and y (reduces
x and y to be coprime) and returns the tuple (x, y)
'''
def reducedForm(primesArray, x, y):
    for i in primesArray:
        while x % i == 0:
            if y % i == 0:
                x = x / i
                y = y / i
            else:
                break
    if y % x == 0:
        y = y / x
        x = x / x
    return (x, y)

'''
Finds and returns the denominator of the reduced form of the product of all fractions of the form i/j
such that 10 < i < j < 100 and removing the same digit from i and j, i' and j', yields i/j = i'/j'
'''
def findProductCancellableFractions():
    productNumerator = 1
    productDenominator = 1
    for i in xrange(11, 100):
        for j in xrange(i + 1, 100):
            if isCancellable(i, j):
                productNumerator *= i
                productDenominator *= j
    return reducedForm(findPrimes(isqrt(productDenominator) + 1), productNumerator, productDenominator)[1]

print findProductCancellableFractions()