#https://projecteuler.net/problem=50

from tools import findPrimes

#Finds and returns the prime that is smaller than n and is the sum of the most consecutive primes
def findConsecPrimeSum(n):
    primesArray = findPrimes(n)
    numPrimes = len(primesArray)
    
    #Creates a set containing the primes for constant-time lookup of whether a sum is prime
    primesSet = set(primesArray)
        
    maxConsec = 1
    maxSum = 0
    
    '''
    Iterate through the array of primes, in ascending order, to serve as the base. For each base, add
    subsequent primes to the base, checking after each addition whether the sum is a prime. Keep track
    of the longest run whose sum is prime as well as the sum itself.
    '''
    for i in xrange(numPrimes):
        
        '''
        Optimization: Since subsequent primes are larger than the base, if (base * the current
        maxConsec) > n, for all bases > the current base, it is impossible to obtain a run longer than
        the current maxConsec while keeping the sum under n.
        '''
        if (primesArray[i] > n / maxConsec):
            break
        
        j = 0
        currentSum = 0
        while ((currentSum < n) and (i + j < numPrimes)):
            currentSum += primesArray[i + j]
            if currentSum in primesSet:
                if j > maxConsec:
                    maxConsec = j
                    maxSum = currentSum
            j += 1
            
    return maxSum, maxConsec
        
print findConsecPrimeSum(1000000)