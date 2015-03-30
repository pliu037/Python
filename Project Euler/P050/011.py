#https://projecteuler.net/problem=11

from tools import get2DData

'''
Finds the maximum product of <length>-consecutive elements horizontally, vertically, or diagonally
in the rectangle and returns the value
'''
def findProduct(rectangle, length):
    currentMax = 0
    for x in xrange(len(rectangle)):
        for y in xrange(len(rectangle[x])):
            
            #Checks all vertical (x represents rows, so going along x is vertical) products
            if (x + length <= len(rectangle)):
                product = 1
                for i in xrange(length):
                    product *= rectangle[x + i][y]    
                if product > currentMax:
                    currentMax = product
                        
            #Checks all horizontal (y represents columns, so going along y is horizontal) products
            if (y + length <= len(rectangle[x])):
                product = 1
                for i in xrange(length):
                    product *= rectangle[x][y + i]
                if product > currentMax:
                    currentMax = product
                        
            #Checks down-and-to-the-right diagonal products
            if ((x + length <= len(rectangle)) and (y + length <= len(rectangle[x]))):
                product = 1
                for i in xrange(length):
                    product *= rectangle[x + i][y + i]
                if product > currentMax:
                    currentMax = product
                    
            #Checks down-and-to-the-left diagonal products
            if ((x + length <= len(rectangle)) and (y - length + 1 >= 0)):
                product = 1
                for i in xrange(length):
                    product *= rectangle[x + i][y - i]
                if product > currentMax:
                    currentMax = product
                    
    return currentMax
      
print findProduct(get2DData(), 4)