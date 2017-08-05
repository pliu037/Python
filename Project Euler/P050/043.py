#https://projecteuler.net/problem=43

from itertools import permutations

'''
Finds and returns the sum of all permutations of '0123456789' that satisfy: n[1:4] divisible by 2,
n[2:5] divisible by 3, n[3:6] divisible by 5, n[4:7] divisible by 7, n[5:8] divisible by 11, n[6:9]
divisible by 13, and n[7:10] divisible by 17
Method:
Generate 0-9 pandigitals that satisfy the conditions rather than checking all permutations.
'''
def sumSatisfiesCondition():
    currentSum = 0

    return currentSum

# TODO
'''
Checks if n satisfies the following conditions and returns True if it does: n[1:4] divisible by 2,
n[2:5] divisible by 3, n[3:6] divisible by 5, n[4:7] divisible by 7, n[5:8] divisible by 11, n[6:9]
divisible by 13, and n[7:10] divisible by 17
'''
def satisfiesConditions(n):
    if (int(n[3]) % 2 != 0) or \
       ((int(n[2]) + int(n[3]) + int(n[4])) % 3 != 0) or \
       (int(n[5]) % 5 != 0) or \
       (int(n[4:7]) % 7 != 0) or \
       (int(n[5:8]) % 11 != 0) or \
       (int(n[6:9]) % 13 != 0) or \
       (int(n[7:10]) % 17 != 0):
        return False
    return True

'''
Finds and returns the sum of all permutations of '0123456789' that satisfy the conditions specified
in satisfiesConditions(n)
'''
def sumSatisfiesConditionBrute():
    currentSum = 0
    permIter = permutations('0123456789')
    for i in permIter:
        if i[0] != '0':
            check = ''.join(i)
            if satisfiesConditions(check):
                currentSum += int(check)
    return currentSum

#print sumSatisfiesCondition()
print sumSatisfiesConditionBrute()