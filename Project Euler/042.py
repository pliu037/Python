#https://projecteuler.net/problem=42

from gmpy2 import is_square
from gmpy2 import isqrt
from gmpy2 import f_mod
from tools import getWordData
from tools import getWordValue

'''
Checks whether n is a triangular number (f(i) = i*(i + 1)/2 = n where i is a positive integer) and
returns True if it is
Method:
Use the quadratic formula to solve for i. Since i is an integer, check whether the discriminant
(-b - 4*a*c = 1 + 8*n) is a perfect square. If it is, check if the numerator (-b + discriminant =
1 + discriminant) divides the denominator (2*a = 2) perfectly. Since i is positive, (-b - discriminant)
isn't checked since it would be negative.
'''
def isTriangular(n):
    if is_square(1 + 8*n):
        disc = isqrt(1 + 8*n)
        if (f_mod(disc + 1, 2) == 0):
            return True
    return False

#Given a list of words, returns the number of words whose value is a triangular number
def findTriangularWords(words):
    count = 0
    for word in words:
        if isTriangular(getWordValue(word)):
            count += 1
    return count

print findTriangularWords(getWordData())    