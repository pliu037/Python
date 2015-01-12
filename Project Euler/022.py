#https://projecteuler.net/problem=22

import re

'''
Gets the name data from the file data.txt located on the desktop
Removes all "s from the list then splits the list into an array of names
Returns the array
'''
def getData ():
    f = open('C:/Users/Peng/Desktop/data.txt', 'r')
    data = []
    line = f.readline()
    while line != '':
        line = re.sub('["]', '', line)
        data = line.split(',')
        line = f.readline()
    f.close()
    return data

#Finds the sum of the value of the letters of a name, with A = 1 through Z = 26, and returns the value
def getNameValue (name):
    currentSum = 0
    for i in name:
        currentSum += ord(i) - ord('A') + 1
    return currentSum

'''
Finds the sum of the value of the names, with each name being worth its value * its position in an
ascending alphabetically-sorted list, and returns the value
'''
def getTotalValue (names):
    names.sort()
    currentSum = 0
    for i in xrange(len(names)):
        currentSum += getNameValue(names[i]) * (i + 1)
    return currentSum

print getTotalValue(getData())