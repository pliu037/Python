#https://projecteuler.net/problem=40

'''
Finds and returns the n-th digit of the series 123456789101112131415...
Method:
Starting at i = 0, each magnitude block contains (10**(i + 1) - 10**i)*(i + 1) digits. If
n > (10**(i + 1) - 10**i)*(i + 1), then the target digit is located at least in the next magnitude
block. If this is the case, (10**(i + 1) - 10**i)*(i + 1) is subtracted from n and i is
incremented by 1. Repeat the process until n <= (10**(i + 1) - 10**i)*(i + 1). Since each number
within a magnitude block, i, consists of i + 1 digits, the number in which the target digit is
found is given by ((n - 1)/(magnitude + 1) + 10**magnitude) and its position within this number by
(n - 1)%(magnitude + 1).
'''   
def getDigit(n):
    magnitude = 0
    while True:
        if (n - (10**(magnitude + 1) - 10**magnitude)*(magnitude + 1) <= 0):
            number = (n - 1)/(magnitude + 1) + 10**magnitude
            digit = (n - 1)%(magnitude + 1)
            return int(str(number)[digit])
        n -= (10**(magnitude + 1) - 10**magnitude)*(magnitude + 1)
        magnitude += 1

'''    
Finds and returns the product of the digits at positions 10**i for 0 <= i <= n of the series
123456789101112131415...
Observation:
Runs in O(n) time as opposed to the O(10**n) time of the below solution.
'''
def getDigitProduct(n):
    prod = 1
    for i in xrange(n + 1):
        prod *= getDigit(10**i)
    return prod

'''    
Finds and returns the product of the digits at positions 10**i for 0 <= i <= n of the series
123456789101112131415...
'''
def getDigitProductBrute(n):
    num = []
    i = 0
    while len(num) <= 10**n:
        for j in str(i):
            num.append(j)
        i += 1
    prod = 1
    for i in xrange(n + 1):
        prod *= int(num[10**i])    
    return prod

print getDigitProduct(6)
print getDigitProductBrute(6)