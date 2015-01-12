#https://projecteuler.net/problem=14

'''
Recursively finds the length of the Collatz sequence given a starting integer and returns the value
Method:
Given a starting integer, check numLine to see if the length of the Collatz sequence from that integer
is known. If so, return that length, otherwise recursively call collatzRule with a new starting
integer as determined by the Collatz rule (x/2 if x is even and 3x + 1 if x is odd). Every recursive
call tracks of the number of steps required to reach it and, if called from an integer represented
in numLine, stores that value.
Since an integer is either even or odd and it can only lead to one other integer. By induction, only
one Collatz sequence can exist from a given integer.
Observation:
In the other direction, two integers could lead to the same point (3 is odd: 3*3 + 1 = 10; 20 is even:
20/2 = 10). As a result, working backward appears to be more difficult than going forward.
'''
def collatzRule (numLine, start):
    
    #Start has landed within numLine
    if start < len(numLine):
        
        #Start has landed at an element that has already been calculated
        if numLine[start] != 0:
            return numLine[start]
        
        #Start has landed at an element that hasn't yet been calculated
        else:
            if start % 2 == 0:
                check = start / 2
            else:
                check = 3 * start + 1
            numLine[start] = collatzRule (numLine, check) + 1
            return numLine[start]
        
    #Start has landed outside numLine
    if start >= len(numLine):
        if start % 2 == 0:
            check = start / 2
        else:
            check = 3 * start + 1
        return collatzRule (numLine, check) + 1

'''
Finds the integer under the ceiling that generates the longest Collatz sequence and returns that
integer
Method:
Generate an array of 0s of length <ceiling> with indices representing starting integers and values
representing the length of the Collatz sequence starting from that integer. Pre-populate the array by
setting the values at indices 2**i to i + 1 (the number of elements in the Collatz sequence starting
at 2**i). Determine the length of the Collatz sequence starting at x = 3 for 3 <= x < ceiling.
'''
def collatz (ceiling):
    numLine = [0 for _i in xrange(ceiling)]
    i = 0
    while 2**i < ceiling:
        numLine [2**i] = i + 1
        i += 1
    for i in xrange(3, ceiling):
        collatzRule (numLine, i)
    return numLine.index(max(numLine))
print collatz(1000000)