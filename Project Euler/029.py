#https://projecteuler.net/problem=29

from gmpy2 import mpz

'''
Finds and returns the number of distinct terms for a**b with 2 <= a, b <= n
Observation:
Alternatively, could subtract the number of repetitions from (n - 1)**2. This should be both more
memory efficient and more processor efficient.
'''
def distinctTerms(n):
    terms = set()
    for i in xrange(2, n + 1):
        for j in xrange(2, n + 1):
            terms.add(mpz(i**j))
    return len(terms)

print distinctTerms(100)