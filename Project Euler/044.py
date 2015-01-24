#https://projecteuler.net/problem=44

from gmpy2 import is_square
from gmpy2 import isqrt
from gmpy2 import f_mod

'''
Checks whether n is a pentagonal number (f(i) = i*(3*i - 1)/2 = n where i is a positive integer) and
returns True if it is (see 045.py)
'''
def isPent(n):
    x = 2*n
    if is_square(1 + 12*x):
        disc = isqrt(1 + 12*x)
        if (f_mod(disc + 1, 6) == 0):
            return True
    return False

#Generates and returns the n-th pentagonal number (f(n) = n*(3*n - 1)/2)
def getPent(n):
    return n*(3*n - 1)/2

#Checks whether x + y and |x - y| are pentagonal numbers and returns True if they are
def isSumDifferencePent(pentSet, x, y):
    if ((abs(x - y) not in pentSet) or (not isPent(x + y))):
        return False
    return True

'''
Finds and returns the smallest absolute difference between two pentagonal numbers, x and y, such that
x + y and |x - y| are also pentagonal
'''
def findSmallest():
    pentNumbers = []
    pentSet = set()
    i = 0
    
    #Until the inner condition is met, append the (i + 1)-th to pentNumbers at index i
    while True:
        pentNumbers.append(getPent(i + 1))
        pentSet.add(getPent(i + 1))
        j = i - 1
        
        '''
        Inner condition: For each pentagonal number appended at index i, check if (pentNumbers[i] +
        pentNumbers[j]) and (pentNumbers[i] - pentNumbers[j]) are pentagonal numbers for 0 <= j < i
        for descending j. Because pentNumbers is an increasing series, this guarantees that of the
        first i pentagonal numbers, the pair with the smallest difference that satisfies the above
        conditions is found first. This difference is stored in currentMin.
        '''
        while j > 0:
            if (isSumDifferencePent(pentSet, pentNumbers[i], pentNumbers[j])):
                currentMin = pentNumbers[i] - pentNumbers[j]
                
                '''
                It is possible that higher pairs of pentagonal numbers, x and y, can also satisfy
                x + y and |x - y| being pentagonal numbers with a lower |x - y| than currentMin. Since
                the difference between successive pentagonal numbers increases, need to continue
                checking pentagonal numbers until (pentNumbers[i] - pentNumbers[i - 1] >= currentMin).
                '''
                i += 1
                pentNumbers.append(getPent(i + 1))
                while (pentNumbers[i] - pentNumbers[i - 1] < currentMin):
                    j = i - 1
                    while (pentNumbers[i] - pentNumbers[j] < currentMin):
                        if (isSumDifferencePent(pentSet, pentNumbers[i], pentNumbers[j])):
                            if (pentNumbers[i] - pentNumbers[j] < currentMin):
                                currentMin = pentNumbers[i] - pentNumbers[j]
                        j -= 1
                        
                    i += 1
                    pentNumbers.append(getPent(i + 1))
                    
                return currentMin
            j -= 1
            
        i += 1

print findSmallest()