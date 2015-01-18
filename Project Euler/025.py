#https://projecteuler.net/problem=19

from gmpy2 import mpz

'''
Finds the next Fibonacci number given a cache of the previous two, pushes the oldest number off of the
two-object cache, pushes the new number on, and then returns the cache
'''
def fib(cache):
    currentFib = cache[0] + cache[1]
    cache[0] = cache[1]
    cache[1] = currentFib
    return cache

'''
Finds and returns i where the i-th Fibonacci number is the first with n digits
The i-th Fibonacci number is calculated recursively using a cache of the two most recent Fibonacci
numbers (to reduce memory usage)
Observation:
Since the Fibonacci sequence can also be defined by a closed form (F(i) = (phi**i - psi**i)/sqrt(5)
where phi = (1 + sqrt(5))/2 and psi (1 - sqrt(5))/2), the answer can also be obtained by solving for i
such that F(i) > 10**999.
'''
def fibMinDigits(n):
    cache = [mpz(1), mpz(1)]
    i = 2
    while (len(cache[1].digits()) < n):
        cache = fib(cache)
        i += 1
    return i

print fibMinDigits(1000)