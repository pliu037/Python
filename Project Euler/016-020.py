'''
https://projecteuler.net/problem=16
https://projecteuler.net/problem=20
'''

from gmpy2 import mpz
from gmpy2 import fac
from tools import findSumDigits

#Finds the power, a**b, and returns it as a mpz
def power(a, b):
    return mpz(a**b)

#Finds n! and returns it as a mpz
def factorial(n):
    return fac(n)

print findSumDigits(power(2, 1000), 1)
print findSumDigits(factorial(100), 1)