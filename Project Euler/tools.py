#Tools used frequently by Project Euler solutions

import re
from itertools import combinations

'''
Gets integer grid data from the file data.txt located on the desktop
Parses each line, splitting it and returning an array of integers
Appends the array associated with each line to a growing 2D array, representing the layout of the data
file (x representing rows, y representing columns)
Returns the 2D array
'''
def get2DData():
    f = open('C:/Users/Peng/Desktop/data.txt', 'r')
    data = []
    line = f.readline()
    while line != '':
        lineParsed = line.split()
        lineParsed = map(int, lineParsed)
        data.append(lineParsed)
        line = f.readline()
    f.close()
    return data

'''
Gets the name data from the file data.txt located on the desktop
Removes all "s from the list then splits the list into an array of names
Returns the array
'''
def getWordData():
    f = open('C:/Users/Peng/Desktop/data.txt', 'r')
    data = []
    line = f.readline()
    while line != '':
        line = re.sub('["]', '', line)
        data = line.split(',')
        line = f.readline()
    f.close()
    return data

#Finds the sum of the value of the letters of a name, with A = 1 through Z = 26, and returns the value
def getWordValue(name):
    currentSum = 0
    for i in name:
        currentSum += ord(i) - ord('A') + 1
    return currentSum

#Checks whether x is a permutation of y and returns True if it is
def isPermutation(x, y):
    bag1 = sorted(str(x))
    bag2 = sorted(str(y))
    return bag1 == bag2

'''
Return an array of all primes, in ascending order, up to n, exclusive
Method:
Generate an array of 1s of length n with indices representing the non-negative integer line and values
indicating whether that index is a potential prime (1 is yes, 0 is no). Starting at i = 2, the number
line is sieved (see sieve of Eratosthenes) to filter out non-primes (value set to 0). The array of
primes is then constructed by including indices along the number line whose value is still 1.
'''
def findPrimes(n):
    numLine = [1 for _i in xrange(n)]
    i = 2
    while i < n:
        if numLine[i] == 1:
            j = i
            while (i * j < n):
                numLine[i * j] = 0
                j += 1
        i += 1

    i = 2
    primes = []
    while i < n:
        if numLine[i] == 1:
            primes.append(i)
        i += 1
    return primes

'''
Given an array of primes up to sqrt(n), finds the prime factors of n and returns them, in ascending
order, as an array
'''
def findPrimeFactors(primesArray, n):
    primeFactors = []
    for i in primesArray:
        while (n % i == 0):
            n = n / i
            primeFactors.append(i)
        if n == 1:
            break
    if n != 1:
        primeFactors.append(n)
    return primeFactors

'''
Given an array of primes up to sqrt(n), finds the proper divisors of n and returns them as an array
Method:
Factor n into its prime components. For each set containing 1 to x - 1 prime components, where x is
the number of prime components of n, the product of the elements in that set is a proper divisor. 1
is also considered a proper divisor.
'''
def findDivisors(primesArray, n):
    primeFactors = findPrimeFactors(primesArray, n)
    
    #Uses a set to remove duplicate products
    divisorPrimeFactors = set()
    for i in xrange(1, len(primeFactors)):
        comboIter = combinations(primeFactors, i)
        for j in comboIter:
            divisorPrimeFactors.add(j)
            
    divisors = [1]
    for i in divisorPrimeFactors:
        currentProduct = 1
        for j in i:
            currentProduct *= j
        divisors.append(currentProduct)
    return divisors