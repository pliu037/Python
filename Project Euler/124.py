# https://projecteuler.net/problem=124

from tools import findPrimes, findPrimeFactors
from gmpy2 import isqrt


def get_sorted_n_by_rad(n):
    """
    Given that rad(x) is the product of the distinct prime factors of x, returns a sorted list of tuples for
    1 <= i <= n where the tuples are of the form (rad(i), i)
    """
    primes = findPrimes(isqrt(n) + 1)
    rad = [(1, 1)]
    for i in xrange(2, n + 1):
        prime_factors = set(findPrimeFactors(primes, i))
        product = 1
        for prime in prime_factors:
            product *= prime
        rad.append(tuple([product, i]))
    rad.sort()
    return rad


print get_sorted_n_by_rad(100000)[9999]
