#https://projecteuler.net/problem=36

from tools import isPalindrome

#Generates <digits>-length palindromes in lexographic order
class PalindromeGenerator:
    def __init__(self, digits):
        self.digits = digits
        self.odd = (digits % 2 != 0)

        #The first half of the palindrome defines the second half, but it can't have leading zeroes
        self.current = 10**((digits + 1)/2 - 1)

    def __iter__(self):
        return self

    def next(self):
        if self.current >= 10**((self.digits + 1)/2):
            raise StopIteration()
        digitArray = ['0' for _i in xrange(self.digits)]
        base = str(self.current)
        self.current += 1
        for i in xrange(len(base)):
            digitArray[i] = base[i]
            digitArray[self.digits - 1 - i] = base[i]
        return int(''.join(digitArray))

'''
Finds and returns the sum of all numbers with up to n digits, inclusive, that are palindromes in
base 10 and base 2
'''
def sumPalindromes(n):
    currentSum = 0
    for digits in xrange(1, n + 1):
        palindromeGen = PalindromeGenerator(digits)
        for check in palindromeGen:
            if isPalindrome(bin(check)[2:]):
                currentSum += check
    return currentSum

print sumPalindromes(6)