#https://projecteuler.net/problem=32

from itertools import combinations
from itertools import permutations
from tools import findPrimes
from tools import findDivisors

'''
Returns whether n contains only unique digits. If <digits> is passed in as an argument, adds each
digit to the set.
'''
def uniqueDigits(n, digits = set()):
    strng = str(n)
    for i in xrange(len(strng)):
        if strng[i] in digits:
            return False
        digits.add(strng[i])
    return True

#Returns whether the numbers in <numbers> are 1-9 pandigital in aggregate
def isPandigital(numbers):
    digits = set()
    for number in numbers:
        if not uniqueDigits(number, digits):
            return False
    for i in xrange(1, 10):
        if str(i)[0] not in digits:
            return False
    return True

'''
Finds and returns the sum of all products whose multiplicand/multiplier/product triplet is 1-9
pandigital
Method:
Since the multiplicand/multiplier/product triplet must be 1-9 pandigital, there can only be 9 digits
between them. As such, the product must be 4 digits long (more than 4 digits, the multiplicand and
multiplier would not have enough digits; less than 4 digits, the multiplicand and multiplier would
have too many digits).
'''
def findSumPandigitalProducts():
    sum = 0
    primes = findPrimes(100)
    digits = "123456789"
    combos = combinations(digits, 4)
    for combo in combos:
        perms = permutations(combo)
        for perm in perms:
            check = int("".join(perm))
            factors = findDivisors(primes, check)
            for factor in factors[1:]:
                if isPandigital([check/factor, factor, check]):
                    sum += check
                    break
    return sum

print findSumPandigitalProducts()