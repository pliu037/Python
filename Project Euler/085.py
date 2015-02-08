#https://projecteuler.net/problem=85

from math import sqrt

'''
Given an x-by-y rectangle, returns the number of subrectangles
Method:
For each i such that 1 <= i <= x, there are n - i + 1 ways of picking a segment of length i along x.
Therefore, there are x(x + 1) distinct segments along x. Since the same is true for y and a distinct
subrectangle is defined by each distinct pair of x and y segments, there are x(x + 1)y(y + 1)
subrectangles.
'''
def numSubRectangles(x, y):
    return x*(x + 1)*y*(y + 1)/4

'''
Finds and returns the area of the rectangle that has the closest number of subrectangles to n
Method:
By solving 4n = x(x + 1)y(y +1) over R for some x, we obtain the two closest integer solutions to the
problem given that x. Taking a = x(x + 1) and b = y(y + 1), it can be seen that when a < sqrt(n),
b > sqrt(n), and vice versa. Due to the symmetrical nature of a and b, only values of a < sqrt(n)
need to be checked. Given a = x(x + 1) = x'**2 <=> x' > x and the symmetry of a and b, instead of
solving a = x(x + 1), we can check up to x' = sqrt(a) = sqrt(sqrt(n)). For each length of x to be
checked, i such that 1 <= i <= x', we calculate the length of y such that y(y + 1) = 4n/(i(i + 1)).
This results in a real solution whose floor and ceil (since x and y must be integers) are the two
closest values to n given the specific choice of i.
'''
def numClosestSubRectangles(n):
    currentMin = n
    minArea = 0
    for i in xrange(1, int(sqrt(sqrt(n)))):
        target = 4.0*n/(i*(i + 1))
        y = int((sqrt(1 + 4*target) - 1)/2)
        if abs(numSubRectangles(i, y) - n) < currentMin:
            currentMin = abs(numSubRectangles(i, y) - n)
            minArea = i*y
        if abs(numSubRectangles(i, y + 1) - n) < currentMin:
            currentMin = abs(numSubRectangles(i, y + 1) - n)
            minArea = i*(y + 1)
    return minArea

print numClosestSubRectangles(2000000)