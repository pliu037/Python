#https://projecteuler.net/problem=25

from gmpy2 import mpz

'''
Finds and returns i where the i-th Fibonacci number is the first with n digits
The i-th Fibonacci number is calculated iteratively using a cache of the two most recent Fibonacci
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
        currentFib = cache[0] + cache[1]
        cache[0] = cache[1]
        cache[1] = currentFib
        i += 1
    return i

print fibMinDigits(1000)