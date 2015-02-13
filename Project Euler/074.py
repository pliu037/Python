#https://projecteuler.net/problem=74

from tools import findSumFacDigits
from itertools import permutations

'''
Finds and returns the permutations of n, including n itself, that do not have leading zeros
'''
def getNonLeadingZeroPerms(n):

    #Uses a set to remove duplicate products
    goodPerms = set()

    perms = permutations(str(n))
    for perm in perms:
        if perm[0] != '0':
            goodPerms.add(int(''.join(perm)))
    return goodPerms

'''
Recursively finds and returns the number of distinct elements in the chain obtained by iteratively
summing the factorials of the digits of n
'''
def followSumFactorialDigits(visited, currentChain, i):

    #Base case: Since i was visited previously, the length of the downstream chain is known
    if i in visited:
        return visited[i]

    '''
    If i was seen before in the current chain, then it belongs to a factorial loop. Not all elements
    in currentChain are necessarily members of the loop, however, so another pass is made to
    determine which ones are. Since each member of the loop can cycle through the elements of the
    loop, their values are set to the length of the loop.
    '''
    if i in currentChain:
        loop = set()
        while i not in loop:
            loop.add(i)
            i = findSumFacDigits(i)
        for i in loop:
            visited[i] = len(loop)
        return len(loop)

    currentChain.add(i)
    result = followSumFactorialDigits(visited, currentChain, findSumFacDigits(i)) + 1

    '''
    Optimization: The sum of the factorials of the digits of numbers consisting of the same digits
    is the same. Thus, all permutations of i without leading zeros that are not part of a loop have
    the same chain length. Those that are part of a loop have a different chain length. As an
    example, given a and b are permutations:
    a -> x -> y -> b -> x and b -> x -> y -> b
    Permutations that are part of a loop are assigned a value in a lower recursive call (when the
    loop is first found), so not overwriting existing values handles the above case.
    '''
    for perms in getNonLeadingZeroPerms(i):
        if perms not in visited:
            visited[perms] = result

    return visited[i]

'''
Finds and returns the number of factorial chains starting from below 10**n with <length> distinct
elements
'''
def findNumFactorialDigitChains(n, length):
    count = 0
    visited = {}
    for i in xrange(1, n):
        currentChain = set()
        result = followSumFactorialDigits(visited, currentChain, i)
        if result == length:
            count += 1
    return count

print findNumFactorialDigitChains(1000000, 60)