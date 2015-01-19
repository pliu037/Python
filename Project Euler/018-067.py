'''
https://projecteuler.net/problem=18
https://projecteuler.net/problem=67
'''

from tools import getData

'''
Finds the maximum sum of a path through the triangle and returns the value
Method:
For each row of the triangle, starting at the base, calculate the maximum sum of a path, from the
base, to each element of that row.
  a
b   c
Given an element a in a particular row, it can reached from the base either through b or c, where b
and c themselves represent the maximum sum of a path through the subtrees up to elements b and c,
respectively. After iterating up through the triangle, the value obtained at the peak position is the
maximum sum of a path through the entire triangle.
'''
def findPath(triangle):
    lowerRow = triangle[len(triangle) - 1]
    for x in xrange (len(triangle) - 1):
        upperRow = triangle[len(triangle) - 2 - x]
        answerLine = []
        for y in xrange (len(upperRow)):
            answerLine.append(max(lowerRow[y], lowerRow[y + 1]) + upperRow [y])
        lowerRow = answerLine
    return lowerRow[0]
    
print findPath(getData())