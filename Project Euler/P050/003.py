# https://projecteuler.net/problem=3

from tools import findPrimes, findPrimeFactors
from math import sqrt


def find_largest_prime_factor(n):
    sqrt_n = int(sqrt(n))
    primes = findPrimes(sqrt_n)
    prime_factors = findPrimeFactors(primes, n)
    return prime_factors[-1]


print find_largest_prime_factor(600851475143)
