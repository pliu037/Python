#https://projecteuler.net/problem=53

from gmpy2 import fac

#Calculates and returns x choose n
def choose(x, n):
    currentProduct = 1
    for i in xrange(n):
        currentProduct *= x - i
    return currentProduct/fac(n)

#Finds and returns the number of pairs, x, n, such that x choose n > threshold for 1 <= x <= max
def combinationThreshold(threshold, max):
    total = 0
    x = 0

    '''
    Optimization: Stops at the first x such that x choose x/2 > threshold. As x choose x/2 is the
    maximum value attainable by x choose i where 0 <= i <= x, there is no need to check any value of
    x such that x choose x/2 <= threshold.
    '''
    while choose(x, x/2) <= threshold and x <= max:
        x += 1

    check = x/2
    while x <= max:
        offset = 0

        '''
        Optimization: Finds the highest offset such that x choose (check - offset) > threshold
        (equivalently, the lowest n such that x choose n > threshold). As x choose n increases with
        x, for every iteration, this search can start at the previous iteration's minimal n. Given
        that x choose i <= threshold for i < n < x/2 and the symmetrical nature of choose (for every
        i below x/2 such that x choose i <= threshold, there is an i above x/2 that satisfies the
        same condition), then 2*n of the possible x + 1 values of i yield x choose i <= threshold.
        Observation:
        This should reduce running time from O(max**2) (brute force) to O(max).
        '''
        while choose(x, (check - (offset + 1))) > threshold:
            offset += 1
        check -= offset
        total += x - 2*check + 1

        x += 1
    return total

print combinationThreshold(1000000, 100)