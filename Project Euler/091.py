#https://projecteuler.net/problem=91

from fractions import gcd

'''
Given a n x n square, finds and returns the number of right-angled triangles with one point at the
origin
Method:
Consider four classes of triangle: those whose right angle is 1) at the origin, 2) along the y-axis,
3) along the x-axis, and 4) within the square defined by (x, y) where 1 <= x, y <= n. In group 1,
for every value of y such that 1 <= y <= n, there are n values of x (1 <= x <= n) that result in a
right-angled triangle at the origin (n^2). In group 2, for every value of y such that 1 <= y <= n,
there are n values of x (1 <= x <= n) that result in a right-angled triangle along the y-axis (n^2).
In group 3, for every value of x such that 1 <= x <= n, there are n values of y (1 <= y <= n) that
result in a right-angled triangle along the x-axis (n^2). In group 4, for every point (x, y) where
1 <= x, y <= n, the point forms a right angle for every other point that has slope -_x/_y with the
given point where _x/_y is in its most reduced form. Angled toward lower y and higher x, there are
min(y/_x, (n - x)/_y) points that satisfy this condition. Symmetrically, angled toward higher y and
lower x, there are an equal number of points that satisfy this condition.
'''
def findRightAngleTriangles(n):
    num = 3*n**2
    for y in xrange(1, n + 1):
        for x in xrange(1, n + 1):
            gcf = gcd(x, y)
            _y = y/gcf
            _x = x/gcf
            num += 2*min((n - x)/_y, y/_x)
    return num

print findRightAngleTriangles(50)