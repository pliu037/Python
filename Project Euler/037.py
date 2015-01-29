#https://projecteuler.net/problem=37

from tools import findPrimes

'''
Given sets containing left- and right-truncatable primes with x digits, finds and returns three sets
for left-truncatable, right-truncatable, and truncatable primes with x + 1 digits
Method:
Given sets containing left- and right-truncatable primes with x digits, finds (x + 1)-digit left-
and right-truncatable primes by taking existing left- and right-truncatable primes and adding a
digit on the left or right, respectively, checking that the new number is also a prime. The digits
that can be added on the left or right are restricted by their position within a truncatable prime.
(x + 1)-digit truncatable primes are given by the intersection of (x + 1)-digit left- and right-
truncatable primes.
'''
def findTruncatablePrimes(primesSet, leftTruncatable, rightTruncatable):

    #A truncatable prime cannot contain 4, 6, or 8 in either the left-most position nor the middle
    addLeft = [1, 2, 3, 5, 7, 9]

    '''
    A truncatable prime cannot contain 2, 4, 6, 8, or 5 in either the right-most position nor the
    middle
    '''
    addRight = [1, 3, 7, 9]

    newLeftTruncatable = set()
    newRightTruncatable = set()
    truncatable = []
    for base in leftTruncatable:
        for choice in addLeft:
            check = int(str(choice) + str(base))
            if check in primesSet:
                newLeftTruncatable.add(check)
    for base in rightTruncatable:
        for choice in addRight:
            check = int(str(base) + str(choice))
            if check in primesSet:
                newRightTruncatable.add(check)
                if int((str(base) + str(choice))[1:]) in leftTruncatable:
                    truncatable.append(check)
    return newLeftTruncatable, newRightTruncatable, truncatable

'''
Finds and returns the sum of all 11 truncatable primes (a prime is truncatable if removing any
number of digits from either the left or right side yields another prime)
Method:
Start with those digits that a truncatable prime can end and start with as the sets of left- and
right-truncatable primes, respectively. Every iteration, the set of x-digit left- and right-
truncatable primes is updated to contain only (x + 1)-digit left- and right-truncatable primes
while discovering any (x + 1)-digit truncatable primes.
'''
def findSumTruncatablePrimes():

    #Guessed <the largest truncatable prime> < 1000000, so would only need primes up to 1000000
    primesSet = set(findPrimes(1000000))

    #A truncatable prime must start with 2, 3, 5, or 7 and end with 3 or 7
    leftTruncatable = set([3, 7])
    rightTruncatable = set([2, 3, 5, 7])

    truncatablePrimes = []
    while len(truncatablePrimes) < 11:
        results = findTruncatablePrimes(primesSet, leftTruncatable, rightTruncatable)
        leftTruncatable = results[0]
        rightTruncatable = results[1]
        truncatablePrimes += results[2]
    return sum(truncatablePrimes)

print findSumTruncatablePrimes()