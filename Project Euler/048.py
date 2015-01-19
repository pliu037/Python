#https://projecteuler.net/problem=48

from gmpy2 import mpz

#Finds the sum of i**i for 1 <= i <= n and returns the sum as a string
def findDigits(n):
    currentSum = mpz(0)
    for i in xrange(n):
        currentSum += (i + 1)**(i + 1)
    digits = currentSum.digits()
    return digits

print findDigits(1000)[-10:]