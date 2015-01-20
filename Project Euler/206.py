#https://projecteuler.net/problem=206

from gmpy2 import isqrt
from gmpy2 import mpz

'''
Assuming the third last digit of n is 9 and the last digit of n is 0 (findSqForTemplate enforces this
condition), returns True if n matches the template (1_2_3_4_5_6_7_8_9_0)
'''
def fitsTemplate(n):
    if (n / 10**18 != 1) or \
       ((n / 10**16) % 10 != 2) or \
       ((n / 10**14) % 10 != 3) or \
       ((n / 10**12) % 10 != 4) or \
       ((n / 10**10) % 10 != 5) or \
       ((n / 10**8) % 10 != 6) or \
       ((n / 10**6) % 10 != 7) or \
       ((n / 10**4) % 10 != 8):
        return False
    return True

'''
Finds the integer whose square matches the template, 1_2_3_4_5_6_7_8_9_0 where each _ is a digit, and
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