#https://projecteuler.net/problem=30

from gmpy2 import mpz

#Converts the mpz into a string, sums up the n-th power of the digits, and returns the value
def findSumDigits(i, n):
    digits = i.digits()
    currentSum = 0
    for i in digits:
        currentSum += int(i)**n
    return currentSum

'''
Finds and returns the sum of integers whose sum of the n-th power of their digits is equal to that
integer
Method:
Each digit added increases the number by up to a factor of 10 (10**i where i is the number of digits)
but adds up to 9**n to the sum. Find i such that i*(9**n) < 10**i. Only need to check up to i*(9**n)
as it is the highest attainable sum given i digits.
'''
def findSumPowers(n):
    currentSum = 9**n
    digits = 1
    while currentSum >= 10**digits:
        currentSum += 9**n
        digits += 1

    currentSum = 0
    for i in xrange(2, digits*9**n):
        if (i == findSumDigits(mpz(i), n)):
            currentSum += i
    return currentSum

print findSumPowers(5)
            