#https://projecteuler.net/problem=31

'''
'''
def splitSmaller (array, n):
    
    return 0

'''

Method:

'''
def combinations (n):
    DENOMINATIONS = [200, 100, 50, 20, 10, 5, 2, 1]
    
    numCoins = []
    numDenominations = len(DENOMINATIONS)
    for i in xrange(numDenominations):
        numCoins.append(n / DENOMINATIONS[i])
        n = n / DENOMINATIONS[i]

    combinations = 1
        
    for i in xrange(numDenominations):
        while numCoins[i] > 0:
            return 0

    return combinations
    
print combinations(200)