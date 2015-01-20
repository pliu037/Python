#https://projecteuler.net/problem=49

from tools import findPrimes

#Checks whether x is a permutation of y and returns True if it is
def isPermutation(x, y):
    bag1 = sorted(str(x))
    bag2 = sorted(str(y))
    return bag1 == bag2

'''
Finds all triplets, (x, y, z), such that (10**(n - 1) <= x, y, z < 10**n), (x, y, and z are prime),
and (y - x = z - y), and prints them
'''
def findPrimeSequence(n):
    primesArray = findPrimes(10**n)
    
    #Filter out primes below n / 10
    i = 0
    while primesArray[i] < 10**(n - 1):
        i += 1
    primesArray = primesArray[i:]
    
    #Creates a dictionary containing the primes for constant-time lookup of whether a sum is prime
    primesDic = {}
    for i in primesArray:
        primesDic[i] = 1
    
    '''
    Iterate through the array of primes, in ascending order, to serve as the base. For each base,
    iterate through larger primes to find those that are permutations of the base. When a larger prime
    that is a permutation of the base is found, determine whether the third number in the series
    (2*permuted prime - base) is a permutation of the base, and if so, if it is also prime. If so,
    print the triplet.
    Observation:
    Might be more efficient to generate equivalence classes of permuted primes before looking at the
    differences between members of the same class.
    '''
    numPrimes = len(primesArray)
    for i in xrange(numPrimes):
        j = i + 1
        while j < numPrimes:
            
            '''
            Optimization: Since subsequent primes are larger, if (2*current prime - base) >= 10**n,
            then no series whose second term is larger than the current prime can have a third term
            less than 10**n.
            '''
            if 2*primesArray[j] - primesArray[i] >= 10**n:
                break
            
            if isPermutation(primesArray[i], primesArray[j]):
                if isPermutation(primesArray[i], 2*primesArray[j] - primesArray[i]):
                    if ((2*primesArray[j] - primesArray[i]) in primesDic):
                        print primesArray[i], primesArray[j], 2*primesArray[j] - primesArray[i]
            j += 1
    
findPrimeSequence(4)