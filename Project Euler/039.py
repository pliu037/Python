#https://projecteuler.net/problem=39

from gmpy2 import is_square
from math import sqrt

'''
Finds and returns the value of p for which a + b + c = p has the most Pythagorean triplets (a**2 +
b**2 = c**2) for all p <= n
Method:
a + b + c <= n. By the triangle inequality, (a + b >= c) <=> (a + b + c >= 2c) <=> (n >= a + b + c
>= 2c) <=> (n >= 2c) <=> (c <= n/2). If b > a, (a**2 + b**2 = c**2) <=> (2b**2 > c**2) <=> (b >
c/sqrt(2)) and (2a**2 < c**2) <=> (a < c/sqrt(2)). If b < a, b < c/sqrt(2) and a > c/sqrt(2). Thus,
for every b below c/sqrt(2), there is an a above c/sqrt(2) and vice versa. Since a and b are
interchangeable, to avoid double-counting, b is only checked up to c/sqrt(2).
Observation:
Using an algorithm that generates only and all primitive Pythagorean triplets may result in faster
running time.
'''
def findMaxPythagoreanTriplets(n):
    counts = [0 for _i in xrange(n + 2)]
    c = 5
    while c < n/2:
        b = 1
        while (b < c / sqrt(2)):
            if is_square(c**2 - b**2) and sqrt(c**2 - b**2) + b + c <= n:
                counts[int(sqrt(c**2 - b**2)) + b + c] += 1
            b += 1
        c += 1
    return counts.index(max(counts))

print findMaxPythagoreanTriplets(1000)