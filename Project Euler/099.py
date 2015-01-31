#https://projecteuler.net/problem=99

from tools import get2DData
from math import log10

#Given a list of pairs of numbers, x and y, finds and returns the line number with the maximum x**y
def findLargest(data):
    currentMax = 0
    currentLine = 0
    for i in xrange(len(data)):
        check = log10(data[i][0])*data[i][1]
        if check > currentMax:
            currentMax = check
            currentLine = i
    return currentLine + 1

print findLargest(get2DData())