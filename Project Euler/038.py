#https://projecteuler.net/problem=38

from itertools import permutations

'''
Determines whether the given 1-9 pandigital can be written as the concatenation of 1*x, 2*x... n*x
where n > 1
Method:
It is given that 918273645 is a 1-9 pandigital that satisfies these conditions, placing a lower bound
on the maximal solution. Any maximal solution must start with 9. Given this constraint, 
'''
def isPandigitalMultiple(n):
    position = 4
    multiplier = 2
    first = int("".join(n[:4]))
    while True:
        check = str(first*multiplier)
        for j in xrange(len(check)):
            if position >= len(n) or check[j] != n[position]:
                return False
            position += 1
        if position == len(n):
            return True
        multiplier += 1

'''
Finds and returns the largest 1-9 pandigital that can be written as the concatenation of 1*x, 2*x...
n*x where n > 1
'''
def largestPandigitalMultiple():

    #Starts with the largest 1-9 pandigital and iteratively checks the next largest candidate
    digits = "987654321"
    perms = permutations(digits)

    for perm in perms:
        if isPandigitalMultiple(perm):
            return "".join(perm)

print largestPandigitalMultiple()