import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def getDistance(self, other):
        return math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)

p1 = Point(1, 5)
p2 = Point(2, 8)
p3 = Point(10, 3)

distances = [p1.getDistance(p2), p1.getDistance(p3), p2.getDistance(p3)]
biggestDistance = 0.0

for i in range(len(distances)):
    if distances[i] > biggestDistance:
        biggestDistance = distances[i]

print("Code 4.13:", biggestDistance)

points = [Point(0, 0), Point(1, 5), Point(2, 8), Point(10, 3)]
biggestDistanceNested = 0.0

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = points[i].getDistance(points[j])
        if dist > biggestDistanceNested:
            biggestDistanceNested = dist

print("Code 4.14:", biggestDistanceNested)