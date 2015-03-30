#https://projecteuler.net/problem=45

from gmpy2 import is_square
from gmpy2 import isqrt
from gmpy2 import f_mod

'''
Checks whether n is a hexagonal number (f(i) = i*(2*i - 1) = n where i is a positive integer) and
returns True if it is
Method:
Use the quadratic formula to solve for i. Since i is an integer, check whether the discriminant
(-b - 4*a*c = 1 + 8*n) is a perfect square. If it is, check if the numerator (-b + discriminant =
1 + discriminant) divides the denominator (2*a = 4) perfectly. Since i is positive, (-b - discriminant)
isn't checked since it would be negative.
'''
def isHex(n):
    if is_square(1 + 8*n):
        disc = isqrt(1 + 8*n)
        if (f_mod(disc + 1, 4) == 0):
            return True
    return False

'''
Checks whether n is a pentagonal number (f(i) = i*(3*i - 1)/2 = n where i is a positive integer) and
returns True if it is (uses the same method, logically, as isHex)
'''
def isPent(n):
    x = 2*n
    if is_square(1 + 12*x):
        disc = isqrt(1 + 12*x)
        if (f_mod(disc + 1, 6) == 0):
            return True
    return False

'''
Starting from the n-th triangular number (f(n) = n*(n + 1)/2), find and return the next number that is
triangular, pentagonal, and hexagonal
'''
def getNextTriPentHex(n):
    start = n + 1
    while True:
        check = (start * (start + 1))/2
        if (isPent(check) and isHex(check)):
            return check
        start += 1
    
print getNextTriPentHex(285)