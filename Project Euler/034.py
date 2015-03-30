#https://projecteuler.net/problem=34

from gmpy2 import fac
from tools import findSumFacDigits
from tools import isPermutation
from itertools import combinations_with_replacement

'''
Finds and returns the maximum number of digits of an integer whose sum of the factorial of its digits
is equal to itself
Method:
Each digit added increases the number by up to a factor of 10 (10**i where i is the number of digits)
but adds up to 9! to the sum. Find i such that i*9! < 10**i.
'''
def findMaxDigits():
    check = fac(9)
    digits = 1
    while check >= 10**digits:
        check += fac(9)
        digits += 1
    return digits

'''
Finds and returns the sum of integers whose sum of the factorial of their digits is equal to that
integer
Method:
Generates combinations of up to <digits> digits chosen from 1-9 with replacement and finds the sum
of their factorials. Since any permutation of the combination yields the same sum, if the sum is a
permutation of the combination, the sum is an integer whose sum of the factorial of its digits is
equal to itself. While the number of digits in the combination being checked is less than the number
of digits in the sum, adding 0s to the combination being checked may lead to the sum becoming a
permutation of the digits (adding digits chosen from 1-9 is covered by the combination generator).
For each added 0, the sum to check is increased by 0! = 1.
'''
def findSumFactorials(digits):
    currentSum = 0
    digitChars = "123456789"
    for numDigits in xrange(1, digits + 1):
        combos = combinations_with_replacement(digitChars, numDigits)
        for combo in combos:
            check = "".join(combo)
            facSum = findSumFacDigits(int(check))
            while True:
                if isPermutation(int(check), facSum):
                    currentSum += facSum
                    break
                check += '0'
                facSum += 1
                if len(check) > len(str(facSum)):
                    break
    return currentSum - 3

'''
Finds and returns the sum of integers whose sum of the factorial of their digits is equal to that
integer
Method:
Only need to check up to <digits>*9! as it is the highest attainable sum given <digits> digits.
'''
def findSumFactorialsBrute(digits):
    currentSum = 0
    for i in xrange(3, digits*fac(9)):
        if (i == findSumFacDigits(i)):
            currentSum += i
    return currentSum

digits = findMaxDigits()
print findSumFactorials(digits)
print findSumFactorialsBrute(digits)