#https://projecteuler.net/problem=11

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
Finds the maximum product of <length>-consecutive elements horizontally, vertically, or diagonally
in the given rectangle.
'''
def findProduct (rectangle, length):
    max = 0
    
    for x in xrange(len(rectangle)):
        for y in xrange(len(rectangle[x])):
            
            #Checks all vertical (x represents rows, so going along x is vertical) products
            if (x + length <= len(rectangle)):
                product = 1
                for i in xrange(length):
                    product *= rectangle[x + i][y]    
                if product > max:
                    max = product
                        
            #Checks all horizontal (y represents columns, so going along y is horizontal) products
            if (y + length <= len(rectangle[x])):
                product = 1
                for i in xrange(length):
                    product *= rectangle[x][y + i]
                if product > max:
                    max = product
                        
            #Checks down-and-to-the-right diagonal products
            if ((x + length <= len(rectangle)) and (y + length <= len(rectangle[x]))):
                product = 1
                for i in xrange(length):
                    product *= rectangle[x + i][y + i]
                if product > max:
                    max = product
                    
            #Checks down-and-to-the-left diagonal products
            if ((x + length <= len(rectangle)) and (y - length + 1 >= 0)):
                product = 1
                for i in xrange(length):
                    product *= rectangle[x + i][y - i]
                if product > max:
                    max = product
                    
    return max
      
print findProduct(getData(), 4)