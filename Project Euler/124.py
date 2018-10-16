# https://projecteuler.net/problem=124

from tools import findPrimes, findPrimeFactors
from gmpy2 import isqrt


def get_sorted_n_by_rad(n):
    """

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
