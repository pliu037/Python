import math

'''
I Googled the formula for determining the distance between points, whose positions are given in
longitude and lattitude
point1 and point2 are both tuples of the form (lon, lat)
Longitude and lattitude are given as real numbers (degrees); this method does not accept degree/
minute/second, but an adaptor method can be added to convert degree/minute/second to degree
Returns the distance between the two points in m
'''
def haversine(point1, point2):
    R = 6371000 #radius of the Earth in m
    phi1 = math.radians(point1[1])
    phi2 = math.radians(point2[1])
    deltaPhi = math.radians(point2[1] - point1[1])
    deltaLambda = math.radians(point2[0] - point1[0])

    a = math.sin(deltaPhi/2)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(deltaLambda/2)**2
    c = 2*math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R*c

'''
points is an array of 4 points, each of which is a tuple of the form (lon, lat)
The first driver is going from index 0 to index 1
The second driver is going from index 2 to index 3
If the first driver is picking up and dropping off the second driver, the path is 0 - 2 - 3 - 1
If the second driver is picking up and dropping off the first driver, the path is 2 - 0 - 1 - 3
Because the distance between points is symmetric (i.e.: d(0, 2) = d(2, 0)), the difference between
the first driver's detour distance and the second driver's detour distance is the difference between
d(2, 3) and d(0, 1)
Returns the shorter of the two paths in m
'''
def shortest(points):
    distance = 0
    distance += haversine(points[0], points[2])
    distance += haversine(points[1], points[3])
    distance += min(haversine(points[2], points[3]), haversine(points[0], points[1]))
    return distance

points = [(10, 10), (20, 20), (30, 30), (40, 40)]
print shortest(points)
