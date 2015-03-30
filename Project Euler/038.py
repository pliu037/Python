#https://projecteuler.net/problem=38

from itertools import permutations

'''
Determines whether <num> can be written as the concatenation of 1*x, 2*x... n*x where n > 1 and x is
the number formed by the first i digits of <num>
'''
def isMultipleConcat(num, i):
    position = i
    multiplier = 2
    first = int("".join(num[:i]))
    while True:
        check = str(first*multiplier)
        for j in xrange(len(check)):
            if position >= len(num) or check[j] != num[position]:
                return False
            position += 1
        if position == len(num):
            return True
        multiplier += 1

'''
Finds and returns the largest 1-9 pandigital that can be written as the concatenation of 1*x, 2*x...
n*x where n > 1
Method:
Since it is given that 918273645 is a 1-9 pandigital that satisfies these conditions, any maximal
solution must start with 9. Combined with the fact that each sequence starts with 1*x, x must start
with 9. Any i-digit number starting with 9 multiplied by n <= 10 contains i + 1 digits. Since
918273645 is the unique sequence resulting from a 1-digit x, alternative solutions must have i > 1
digits. For i = 2, 3, 4, or 5+, the number of digits in subsequent terms is 3, 4, 5, or 6+,
respectively. 2 + 3*(n - 1) = 9, 3 + 4*(n - 1) = 9, and 5 + 6*(n - 1) = 9 (the length of a 1-9
pandigital) has no solution for integer values of n such that 1 < n <= 10 whereas 4 + 5*(n - 1) = 9
does have a solution, indicating that x must be 4 digits long.
'''
def largestPandigitalMultiple():

    #Starts with the largest 1-9 pandigital and iteratively checks the next largest candidate
    digits = "987654321"
    perms = permutations(digits)

    for perm in perms:
        if isMultipleConcat(perm, 4):
            return "".join(perm)

print largestPandigitalMultiple()