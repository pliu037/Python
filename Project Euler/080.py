#https://projecteuler.net/problem=80

from gmpy2 import mpfr
from gmpy2 import sqrt
from gmpy2 import is_square
import gmpy2

#Given a string representation of a number, returns the sum of its digits
def getDigitSum(strng):
    currentSum = 0
    for digit in strng:
        currentSum += int(digit)
    return currentSum

'''
Finds and returns the sum of the n left-most digits of the square roots of the natural numbers up to
m, inclusive, but not including perfect squares
'''
def getDigitSums(m, n):

    '''
    gmpy2's precision is specified in bits, so to attain an accuracy of n digits requires
    log(10)/log(2) bits < 4 bits per digit.
    '''
    gmpy2.get_context().precision = 4*n
    currentSum = 0
    for i in range(1, m + 1):
        if not is_square(i):
            x = mpfr(i)
            x = sqrt(x)
            x = x.digits()
            currentSum += getDigitSum(x[0][:n])
    return currentSum

print getDigitSums(100, 100)