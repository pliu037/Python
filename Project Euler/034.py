#https://projecteuler.net/problem=34

from gmpy2 import fac

#Converts the mpz into a string, sums up the factorial of the digits, and returns the value
def findSumDigits(i):
    digits = str(i)
    currentSum = 0
    for i in digits:
        currentSum += fac(int(i))
    return currentSum

'''
Finds and returns the sum of integers whose sum of the factorial of their digits is equal to that
integer
Method:
Each digit added increases the number by up to a factor of 10 (10**i where i is the number of digits)
but adds up to 9! to the sum. Find i such that i*9! < 10**i. Only need to check up to i*9! as it is
the highest attainable sum given i digits.
'''
def findSumFactorials():
    currentSum = fac(9)
    digits = 1
    while currentSum >= 10**digits:
        currentSum += fac(9)
        digits += 1

    currentSum = 0
    for i in xrange(3, digits*fac(9)):
        if (i == findSumDigits(i)):
            currentSum += i
    return currentSum

print findSumFactorials()