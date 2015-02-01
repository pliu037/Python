#https://projecteuler.net/problem=100

from gmpy2 import mpz
from gmpy2 import is_square
from gmpy2 import isqrt

'''

Method:
Brute force search is way too slow.
'''
def findNextDoubleDraw(n):
    n = mpz(n)
    while True:
        discriminant = (n**2 - n)*2 + 1
        if is_square(discriminant):
            check = isqrt(discriminant) + 1
            if check % 2 == 0:
                return check / 2, n
        n += 1

print findNextDoubleDraw(10**12)