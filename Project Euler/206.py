#https://projecteuler.net/problem=206

from gmpy2 import isqrt
from gmpy2 import mpz

'''
Assuming n has the same number of digits as the template (findSqForTemplate enforces this condition),
returns True if n matches the template
'''
def fitsTemplate(n):
    strng = n.digits()
    template =['1','','2','','3','','4','','5','','6','','7','','8','','9','','0']
    for i in xrange(len(template)):
        if template[i] != '':
            if strng[i] != template[i]:
                return False
    return True

'''
Finds the integer whose square matches the template 1_2_3_4_5_6_7_8_9_0, where each _ is a digit, and
returns its value
Method:
Since the template, 1_2_3_4_5_6_7_8_9_0, ends with 0, it's isqrt must end with 0. As such, the second
last digit of the target must be 0. Since the target's third-last digit is 9, the second last digit of
the isqrt must be 3 or 7. Since the smallest possible number that fits the template is
1020304050607080900, the search starts at 1010101030, the smallest integer that is greater than
sqrt(1020304050607080900) that fits the constraints of the isqrt.
'''    
def findSqForTemplate():
    current = 1010101030
    check = mpz(current**2)
    while current < isqrt(1929394959697989900):
        if fitsTemplate(check):
            return current
        
        #Optimization: Uses addition to construct the next square to check rather than resquaring.
        check = check + 2*40*current + 40**2
        
        current += 40
        if fitsTemplate(check):
            return current
        check = check + 2*60*current + 60**2
        current += 60

print findSqForTemplate()