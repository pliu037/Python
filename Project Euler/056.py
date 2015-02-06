#https://projecteuler.net/problem=56

from tools import findSumDigits

#Finds and returns the maximum sum of digits of a**b for 1 <= a, b < n
def maxDigitSum(n):
    currentMax = 0
    for i in xrange(1, n):
        for j in xrange(1, n):
            check = findSumDigits(i**j, 1)
            if check > currentMax:
                currentMax = check
    return currentMax

print maxDigitSum(100)