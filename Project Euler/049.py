#https://projecteuler.net/problem=49

from tools import findPrimes

def findSequence():
    primes = findPrimes(100)
    print primes

findSequence()