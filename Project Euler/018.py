'''
https://projecteuler.net/problem=18
https://projecteuler.net/problem=67
'''

'''
Gets the triangle data from the file data.txt located on the desktop
Parses each line, splitting it and returning an array of integers
Appends the array associated with each line to a growing 2D array, representing the layout of the data
file (x representing rows, y representing columns)
Returns the 2D array
'''
def getData ():
    f = open('C:/Users/Peng/Desktop/data.txt', 'r')
    data = []
    line = f.readline()
    while line != '':
        lineParsed = line.split()
        lineParsed = map(int, lineParsed)
        data.append(lineParsed)
        line = f.readline()
    f.close()
    return data

'''
Finds the maximum sum of a path through the triangle and returns the value
Method:
For each row of the triangle, starting at the base, the algorithm calculates the maximum sum of a path
to each element of that row from the base.
  a
b   c
Given an element a in a particular row, it can reached from the base either through b or c, where b
and c themselves represent the maximum sum of a path through the subtrees up to elements b and c,
respectively. Thus, after iterating up through the triangle, the value obtained at the peak position
is the maximum sum of a path through the entire triangle.
'''
def findPath (triangle):
    lowerRow = triangle[len(triangle) - 1]
    for x in xrange (len(triangle) - 1):
        upperRow = triangle[len(triangle) - 2 - x]
        answerLine = []
        for y in xrange (len(upperRow)):
            answerLine.append(max(lowerRow[y], lowerRow[y + 1]) + upperRow [y])
        lowerRow = answerLine
    return lowerRow[0]
    
print findPath(getData())