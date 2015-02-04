#https://projecteuler.net/problem=39

from gmpy2 import is_square
from gmpy2 import isqrt

'''
Finds and returns the value of p for which a + b + c = p has the most Pythagorean triplets (a**2 +
b**2 = c**2) for all p <= n
Method:

'''
def findMaxPythagoreanTriplets(n):
    counts = [0 for _i in xrange(n + 2)]
    x = 1
    while x < n/3:
        b = 1
        while x + 2*b < n/2:
            if is_square(x + 2*b):
                print b + x + b + isqrt(x*(x + 2*b))
            b += 1
        x += 1
        while not is_square(x):
            x += 1
    return counts.index(max(counts))

print findMaxPythagoreanTriplets(100)