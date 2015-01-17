'''
https://projecteuler.net/problem=16
https://projecteuler.net/problem=20
'''

from gmpy2 import mpz
from gmpy2 import fac

#Finds the power, a**b, and returns it as a mpz
def power (a, b):
    return mpz(a**b)

#Finds n! and returns it as a mpz
def factorial(n):
    return fac(n)

#Converts the mpz into a string, sums up the digits, and returns the value
def sumDigits(num):
    digits = num.digits()
    currentSum = 0
    for i in digits:
        currentSum += int(i)
    return currentSum

print sumDigits(power(2, 1000))
print sumDigits(factorial(100))