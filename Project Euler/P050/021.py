#https://projecteuler.net/problem=21

from tools import findPrimes
from tools import findDivisors

'''
Finds and returns the sum of all amicable numbers (given f(x) being the sum of the proper divisors
of x, an amicable pair consists of a and b such that f(a) = b, f(b) = a, and a != b) under n
'''
def findSumAmicable(n):
    primesArray = findPrimes(n)
    sums = [0 for _i in xrange(n + 1)]
    currentSum = 0
    for i in xrange(1, n):
        if sums[i] == 0:
            sums[i] = sum(findDivisors(primesArray, i))
        check = sums[i]

        if check < n:
            if sums[check] == 0:
                sums[check] = sum(findDivisors(primesArray, check))
            cmp = sums[check]
        else:
            cmp = sum(findDivisors(primesArray, check))

        if i == cmp and check != i:
            currentSum += check
    return currentSum

print findSumAmicable(10000)