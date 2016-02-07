#https://projecteuler.net/problem=91

from itertools import combinations

'''
Returns the y-intercept of the line between p1 and p2 if it intersects the y-axis and None otherwise
Method:
A line segment intersects the y-axis if one endpoint's x value is <= 0 and the other endpoint's x
value is >= 0.
'''
def yIntercept(p1, p2):
    if (p1[0] <= 0 and p2[0] >= 0) or (p1[0] >= 0 and p2[0] <= 0):
        slope = float(p2[1] - p1[1])/(p2[0] - p1[0])
        return p1[1] + (0 - p1[0])*slope
    else:
        return None

'''
Returns True if the triangle encloses the origin and False otherwise
Method:
A triangle encloses the origin if at least one of the three sides intersects the y-axis at y <= 0
and at least one of the remaining two sides intersects the y-axis at y >= 0 (because a triangle is a
closed shape, these two sides must close on either side of the y-axis).
'''
def isEnclosed(triangle):
    pointPairs = combinations(triangle, 2)
    intercepts = []
    for pair in pointPairs:
        intercepts.append(yIntercept(pair[0], pair[1]))
    intercepts = [x for x in intercepts if x != None]
    checkPair = combinations(intercepts, 2)
    for pair in checkPair:
        if (pair[0] <= 0 and pair[1] >= 0) or (pair[0] >= 0 and pair[1] <= 0):
            return True
    return False

#Reads in and returns the list of triangles from the file (each triangle is represented as 3 (x, y)
#tuples)
def getTriangles():
    f = open('C:/Users/pengl/Desktop/data.txt', 'r')
    data = []
    line = f.readline().rstrip('\n')
    while line != '':
        lineParsed = line.split(',')
        lineParsed = map(int, lineParsed)
        triangle = []
        for i in xrange(3):
            triangle.append((lineParsed[2*i], lineParsed[2*i + 1]))
        data.append(triangle)
        line = f.readline().rstrip('\n')
    f.close()
    return data

#Given a list of triangles, returns the number of triangles that enclose the origin
def numIncluded():
    count = 0
    triangles = getTriangles()
    for triangle in triangles:
        if isEnclosed(triangle):
            count += 1
    return count

print numIncluded()