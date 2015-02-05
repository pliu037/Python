#https://projecteuler.net/problem=92

from itertools import combinations_with_replacement
from gmpy2 import fac
from tools import findSumDigits

#Finds and returns the number of permutations of the given set of digits
def numPermutations(combo):
    counts = {}
    for i in xrange(len(combo)):
        if combo[i] in counts:
            counts[combo[i]] += 1
        else:
            counts[combo[i]] = 1
    numPerms = fac(len(combo))
    for i in counts:
        numPerms /= fac(counts[i])
    return numPerms

'''
Finds and returns the size of the set consisting of i such that i < 10**n and the end product of
iteratively summing the squares of its digits is 89
Method:
For every combination of length n, the sum of the squares of its digits is the same for all
permutations of the combination.
'''
def findNumSquareDigitChains(n):
    digits = '0123456789'
    countEightynines = 0
    ones = set([1])
    eightynines = set([89])
    combos = combinations_with_replacement(digits, n)
    for combo in combos:
        result = followSumSquareDigits(ones, eightynines, int(''.join(combo)))
        if result == 89:
            countEightynines += numPermutations(combo)
    return countEightynines

'''
Recursively finds and returns whether iteratively summing the squares of the digits of n terminates
in 1 or 89
'''
def followSumSquareDigits(ones, eightynines, n):

    '''
    Base case: If n hits a result that is known to terminate with 1 or 89, all elements in the
    current chain will also terminate with that value
    '''
    if n in ones:
        return 1
    if n in eightynines:
        return 89

    #Prevents infinite recursion since the sum of the squares of the digits of 0 is still 0
    if n == 0:
        return None

    result = followSumSquareDigits(ones, eightynines, findSumDigits(n, 2))

    #Memoizes whether a given value's chain terminates with 1 or 89
    if result == 1:
        ones.add(n)
    elif result == 89:
        eightynines.add(n)

    return result

'''
Finds and returns the size of the set consisting of i such that i < 10**n and the end product of
iteratively summing the squares of its digits is 89
'''
def findNumSquareDigitChainsBrute(n):
    ones = set([1])
    eightynines = set([89])
    for i in xrange(1, 10**n):
        followSumSquareDigits(ones, eightynines, i)
    count = 0
    for i in eightynines:
        if i < 10**n:
            count += 1
    return count

print findNumSquareDigitChains(7)
print findNumSquareDigitChainsBrute(7)