#https://projecteuler.net/problem=66

from gmpy2 import is_square

'''
Finds and returns the lowest x such that (x**2 - 1) / i is the square of a positive integer
Method:
Brute force search is way too slow.
'''
def findX(i):
    x = 2
    while True:
        print x
        if ((x**2 - 1) % i == 0):
            if is_square((x**2 - 1) / i):
                return x
        x += 1

'''
Finds and returns the value of i that maximizes, for 2 <= i <= n, the minimum value of x that
satisfies (x**2 - 1) / i being a perfect square
'''
def findMaxSolution(n):
    currentMax = 0
    maxI = 0
    for i in xrange(n, n + 1):
        if not is_square(i):
            x = findX(i)
            print i, x
            if x > currentMax:
                currentMax = x
                maxI = i
    return maxI

print findMaxSolution(1000)