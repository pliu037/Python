#https://projecteuler.net/problem=63

from gmpy2 import log10
from math import floor

'''
Finds and returns the number of n-digit integers of the form i**n where i is a positive integer
Method:
A number, i**n, has floor(n*log_10(i)) + 1 digits. Given x = log_10(i), (floor(nx) + 1 = n) <=>
(floor(nx) = n - 1) <=> (n - 1 <= nx < n) <=> (1 - 1/n <= x < 1). (x < 1) <=> (log_10(i) < 1) <=>
(i < 10), but since i is a positive integer, 1 <= i < 10. (1 - 1/n <= x) <=> (1 - x <= 1/n) <=>
(1/(1 - x) >= n). Thus, for all integer values of n such that 1 <= n <= 1/(1 - log_10(i)), of which
there are floor(1/(1 - log_10(i))), i**n will contain n digits.
'''
def findNumPowerDigits():
    count = 0
    for i in xrange(1, 10):
        count += floor(1/(1 - log10(i)))
    return count

print findNumPowerDigits()