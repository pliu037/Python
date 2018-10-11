#https://projecteuler.net/problem=52

from tools import isPermutation

'''
Finds an integer x such that 2x, 3x, 4x, 5x, and 6x are permutations of x and returns its value
Method:
Since 6x must be a permutation of x, the first digit of x must be 1 or 6x gains an extra digit. Since
2x must be a permutation of x, x must contain 2/4/6/8/0. Since 5x must be a permutation of x, x must
contain 5/0. To satisfy these constraints, x must be at least 3 digits long.
'''
def findPermutations():
    magnitude = 2
    check = 10**magnitude
    while True:
        if isPermutation(check, 5*check) and \
           isPermutation(check, 2*check) and \
           isPermutation(check, 4*check) and \
           isPermutation(check, 6*check) and \
           isPermutation(check, 3*check):
            return check
        check += 1
        if check / 10**magnitude > 1:
            magnitude += 1
            check = 10**magnitude
    
print findPermutations()