'''
https://projecteuler.net/problem=81
https://projecteuler.net/problem=82
https://projecteuler.net/problem=83
'''

from tools import get2DData
import heapq

class Node:

    def __init__(self, value, paths):
        self.value = value
        self.paths = paths

def findMinPath(map, start, stop):
    pq = []
    visited = set()
    heapq.heappush(start)
    while heapq:
        return 0

def processData(array, directions):
    map = []
    for i in xrange(len(array)):
        map.append([])
        for j in xrange(len(array[i])):
            map[i].append(Node(array[i][j], ))
    return map