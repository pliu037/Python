#https://projecteuler.net/problem=24

from itertools import permutations
from gmpy2 import fac

'''
Finds and returns the n-th lexographic permutation of strng
Method:
Given a sorted list of length i, there are fac(i - 1) permutations possible without changing the first
position. If n >= fac(i - 1), the first position must change. For every multiple of fac(i - 1), the
first position changes once and consumes fac(i - 1) from n. To enforce lexographic ordering, when i
changes, it must change to the next lowest element. As the list is sorted, this is equivalent to
swapping it with the (n/fac(i - 1) + 1)-th position. After this iteration, the first position will be
the correct value. Sort the remaining i - 1 positions and, using the reduced n, repeat the process for
the sublist of length i - 1. After j iterations, the first j positions will be correct.
Observation:
Runs in O(i) time, where i is the number of elements, as opposed to the O(i!) time of the below
solution.
'''
def lexographicPermutation(strng, n):
    n -= 1
    elements = sorted(strng)
    for i in xrange(len(elements) - 1):
        currentFac = fac(len(elements) - 1 - i)
        if n >= currentFac:
            temp = elements[i]
            elements[i] = elements[n / currentFac + i]
            elements[n / currentFac + i] = temp
            n -= (n / currentFac)*currentFac
            elements[i + 1:] = sorted(elements[i + 1:])
    return elements
    
#Finds and returns the n-th lexographic permutation of strng
def lexographicPermutationBrute(strng, n):
    iterator = permutations(sorted(strng), len(strng))
    for _i in xrange(n - 1):
        iterator.next()
    return iterator.next()
    
print lexographicPermutation('0123456789', 1000000)
print lexographicPermutationBrute('0123456789', 1000000)