#https://projecteuler.net/problem=35

from tools import findPrimes

#Given a number n, shifts the digits to the right and returns the shifted number
def shiftDigits(n):
    digits = list(str(n))
    tempDigit = digits[-1]
    for i in xrange(len(digits)):
        digits[len(digits) - 1 - i] = digits[len(digits) - 2 - i]
    digits[0] = tempDigit
    return int(''.join(i for i in digits))

'''    
Given a prime n, checks each possible shift (e.g.: abc -> cab -> bca) and returns a list of shifts if
they are all prime; returns None otherwise
'''
def getOtherCircularPrimes(primesSet, n):
    circularPrimes = []
    circularPrimes.append(n)
    check = n
    for _i in xrange(1, len(str(n))):
        check = shiftDigits(check)
        if check not in primesSet:
            return None
        circularPrimes.append(check)
    return circularPrimes

#Finds and returns the number of primes less than n whose possible shifts are all prime
def findCircularPrimes(n):
    primesSet = set(findPrimes(n))
    circularPrimes = set()
    for i in primesSet:
        if i not in circularPrimes:
            circulars = getOtherCircularPrimes(primesSet, i)
            if circulars != None:
                for j in circulars:
                    circularPrimes.add(j)        
    return len(circularPrimes)
    
print findCircularPrimes(1000000)