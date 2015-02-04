#https://projecteuler.net/problem=55

from tools import isPalindrome

'''
Recursively "determines" whether n is a Lychrel number and returns True if after <iter> iterations,
it has not produced a palindrome
'''
def isLychrel(iter, n):

    '''
    Base case: If count = 0, exceeded the threshold for testing for non-"Lychrel-ness" and assumes
    it is a Lychrel number, returning True
    '''
    if iter <= 0:
        return True

    rev = str(n)[::-1]
    check = n + int(rev)
    if isPalindrome(str(check)):
        return False

    return isLychrel(iter - 1, check)

'''
Finds and the returns the number of Lychrel numbers below n (a Lychrel number is defined to be any
number, which after 50 iterations of adding the reverse of the value from the previous iteration to
the value from the previous iteration, has not produced a palindrome)
'''
def numLychrels(n):
    count = 0
    for i in xrange(1, n):
        if isLychrel(50, i):
            count += 1
    return count

print numLychrels(10000)