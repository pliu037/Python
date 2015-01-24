#https://projecteuler.net/problem=33

from gmpy2 import mpz
from tools import findPrimes

'''
Determines if x and y are cancellable (removing the same digit from x and y yields x' and y' such that
x/y = x'/y' and returns True if it is
'''
def isCancellable(x, y):
    xDigits = mpz(x).digits()
    yDigits = mpz(y).digits()
    flag = False
    for i in xDigits:
        if i in yDigits:
            flag = True
    if not flag:
        return False
    
    
    return True

'''
Removes all common factors from both x and y (reduced x and y to be coprime) and returns the tuple
(x, y)
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
Finds and returns the product of the denominators of the reduced form of all fractions of form i/j
such that 10 <= i < j < 100 and removing the same digit from i and j yields i' and j' such that i/j =
i'/j'
'''
def findProductCancellableFractions():
    primesArray = findPrimes(10)
    product = 1
    for i in xrange(10, 100):
        for j in xrange(i + 1, 100):
            if isCancellable(i, j):
                product *= reducedForm(primesArray, i, j)[1]
    return product

print findProductCancellableFractions()