'''
https://projecteuler.net/problem=81
https://projecteuler.net/problem=82
https://projecteuler.net/problem=83
'''

from tools import get2DData
import heapq

class Node:
    def __init__(self, value):
        self.value = value
        self.connections = []

    def addConnection(self, connection):
        self.connections.append(connection)

'''
Given a start node, and stop node, finds and returns the value of the minimal path starting from
start, through the map (not explicitly passed, but encoded in the nodes' connections), to stop
Method:
Uses Dijkstra's shortest path algorithm since there are no negative values. The format of a path
is (<value of the path so far>, <last node in the path>).
'''
def findMinPath(start, stop):
    pathsHeap = []
    visited = set()
    heapq.heappush(pathsHeap, start)
    while heapq:
        current = heapq.heappop(pathsHeap)
        currentValue = current[0]
        currentNode = current[1]
        if currentNode == stop:
            return currentValue
        if currentNode not in visited:
            visited.add(currentNode)
            for connection in currentNode.connections:
                if connection not in visited:
                    heapq.heappush(pathsHeap, (currentValue + connection.value, connection))

'''
Given a 2D grid of values and a list of allowed directions, builds and returns a map where each node
contains its value and a list of nodes it can reach
'''
def createMap(array, directions):
    map = []
    x = len(array)
    y = len(array[0])
    for i in xrange(x):
        map.append([])
        for j in xrange(y):
            map[i].append(Node(array[i][j]))
    for i in xrange(x):
        for j in xrange(y):
            for direction in directions:
                checkX = i + direction[0]
                checkY = j + direction[1]
                if checkX >= 0 and checkX < x and checkY >= 0 and checkY < y:
                    map[i][j].addConnection(map[checkX][checkY])
    return map

'''
Finds and returns the value of the shortest path from the top left node to the bottom right node
using only the directions specified
'''
def findPathTLBR(array, directions):
    map = createMap(array, directions)
    start = (map[0][0].value, map[0][0])
    end = map[len(map) - 1][len(map[0]) - 1]
    return findMinPath(start, end)

'''
Finds and returns the value of the shortest path from any node in the left-most column to any node
in the right-most column using only the directions specified
Method:
Virtual start and end nodes with 0 value are created to simulate being able to start at any node in
the left-most column and end at any node in the right-most column. The virtual start node connects
to all of the nodes in the left-most column while all of the nodes in the right-most column connect
to the virtual end node.
'''
def findPathLR(array, directions):
    map = createMap(array, directions)
    startNode = Node(0)
    start = (0, startNode)
    end = Node(0)
    for i in xrange(len(map)):
        startNode.addConnection(map[i][0])
    for i in xrange(len(map)):
        map[i][len(map[i]) - 1].addConnection(end)

    return findMinPath(start, end)

print findPathTLBR(get2DData(), [[1, 0], [0, 1]])
print findPathLR(get2DData(), [[1, 0], [0, 1], [-1, 0]])
print findPathTLBR(get2DData(), [[1, 0], [0, 1], [-1, 0], [0, -1]])