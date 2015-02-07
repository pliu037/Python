'''
https://projecteuler.net/problem=31
https://projecteuler.net/problem=76
https://projecteuler.net/problem=77
'''

from tools import findPrimes

'''
Recursively finds the number of combinations that obtain a target value, i, given the denominations
specified in denomList
'''
def recCombinations(denomList, values, i):

    #Base case: If i = 0, the combination specified by this trace has attained n
    if i == 0:
        return 1

    '''
    Base case: If denomList only contains one more element, the combination specified by this trace
    can only attain n if (i % <the final value in denomList> = 0)
    Observation:
    If denomList includes 1, this cannot occur.
    '''
    if len(denomList) == 1:
        if (i % denomList[0] == 0):
            return 1
        else:
            return 0

    j = 0
    combinations = 0

    '''
    If denomList contains 2 or more elements and a target value, i, the number of viable
    combinations given the trace up to this point is equal to the sum of the number of viable
    combinations using 0 to j units of the largest denomination, leaving denomList[1:] and (i -
    j*denomList[0]) as input into the recursive calls. The sum is returned.
    Optimization: Using memoization, with l (the length of denomList; since denomList is sorted,
    the length uniquely identifies the sublist) and i (here, i actually represents the argument to
    be passed into the recursive call) as indices, if values[(l, i)] has not been calculated before,
    calculate it, store it, and then add it to the sum. Otherwise, just add the memoized value to
    the sum.
    '''
    while j*denomList[0] <= i:
        if (len(denomList), i - j*denomList[0]) in values:
            combinations += values[(len(denomList), i - j*denomList[0])]
        else:
            values[(len(denomList), i - j*denomList[0])] = recCombinations(denomList[1:],
                values, i - j*denomList[0])
            combinations += values[(len(denomList), i - j*denomList[0])]
        j += 1

    return combinations

'''
Given a list of denominations and a target value, n, finds and returns the number of combinations
that yield exactly n
'''
def combinations (denominations, n):
    sortedDenom = sorted(denominations)
    sortedDenom.reverse()
    values = {}
    return recCombinations(sortedDenom, values, n)

#Finds and returns the first integer that can be written as the sum of primes in over n ways
def lowestcombinations(n):
    primesArray = findPrimes(n)
    i = 2
    while (combinations(primesArray, i) <= n):
        i += 1
    return i

print combinations([1, 2, 5, 10, 20, 50, 100, 200], 200)
print combinations([i for i in xrange(1, 100)], 100)
print lowestcombinations(5000)