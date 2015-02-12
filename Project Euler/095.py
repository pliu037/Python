#https://projecteuler.net/problem=95

from tools import findPrimes
from tools import findDivisors
from gmpy2 import isqrt

'''
Recursively finds and returns the amicable loop that i is a member of given that the loop exists and
no members of the loop exceed n
'''
def followChain(primesArray, currentChain, visited, i, n):

    #Base case: If i > n, it cannot be part of an amicable loop with no members greater than n
    if i > n:
        return None

    #Base case: If i was visited in a previous chain, all subsequent elements have too
    if visited[i]:
        return None

    #If i was seen before in the current chain, then it belongs to an amicable loop
    if i in currentChain:
        loop = set()
        while i not in loop:
            loop.add(i)
            i = sum(findDivisors(primesArray, i))
        return loop

    currentChain.add(i)
    result = followChain(primesArray, currentChain, visited, sum(findDivisors(primesArray, i)), n)

    '''
    It is important to set i to visited when unwinding the recursive stack because whether i was
    visited in a previous chain is checked before whether i has been seen in the current chain
    '''
    visited[i] = True

    return result

'''
Finds and returns the lowest element of the longest amicable loop whose members do not exceed n (an
amicable loop is one such that
'''
def findLowestLongest(n):
    maxLoopLength = 0
    visited = [False for _i in xrange(n + 1)]
    primesArray = findPrimes(isqrt(n))
    for i in xrange(1, n + 1):
        if not visited[i]:
            currentChain = set()
            loop = followChain(primesArray, currentChain, visited, i, n)
            if loop and len(loop) > maxLoopLength:
                maxLoopLength = len(loop)
                maxLoop = loop
    return min(maxLoop)

print findLowestLongest(1000000)