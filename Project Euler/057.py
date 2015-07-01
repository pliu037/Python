#https://projecteuler.net/problem=57

'''
Finds and returns the number of terms whose numerator contains more digits than its denominator
within the first n terms of the continued fraction
f(1) = 1 + 1/2 = 3/2
f(2) = 1 + 1/(2 + 1/2) = 7/5
f(3) = 1 + 1/(2 + 1/(2 + 1/2)) = 17/12
f(4) = 1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29
...
Method:
f(n) = a_n/b_n
f(n + 1) = 1 + 1/(1 + f(n)) = 1 + 1/(1 + a_n/b_n) = 1 + 1/((a_n + b_n)/b_n) = 1 + b_n/(a_n + b_n)
= (a_n + 2*b_n)/(a_n + b_n)
Given that a_n and b_n (f(n)) are coprime, we show that a_n + 2*b_n and a_n + b_n (f(n + 1)), must
also be coprime. By contradiction, if a_n + 2*b_n and a_n + b_n have a common factor, x, then
(a_n + 2*b_n)/x and (a_n + b_n)/x are both integers. Thus, (a_n + 2*b_n)/x - (a_n + b_n)/x = b_n/x
and (a_n + b_n)/x - b_n/x = a_n/x are also integers, which is a contradiction. Since a_1 and b_1, 3
and 2 respectively, are coprime, then by induction, a_n and b_n are coprime for all n >= 1.
'''
def sqrtConvergents(n):
    num = 1
    denom = 1
    count = 0
    for i in xrange(n):
        new_num = num + 2*denom
        denom += num
        num = new_num
        if len(str(num)) > len(str(denom)):
            count += 1
    return count

print sqrtConvergents(1000)