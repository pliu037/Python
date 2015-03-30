#https://projecteuler.net/problem=22

from tools import getWordData
from tools import getWordValue

'''
Finds the sum of the value of the names, with each name being worth its value * its position in an
ascending alphabetically-sorted list, and returns the value
'''
def getTotalValue(names):
    names.sort()
    currentSum = 0
    for i in xrange(len(names)):
        currentSum += getWordValue(names[i]) * (i + 1)
    return currentSum

print getTotalValue(getWordData())