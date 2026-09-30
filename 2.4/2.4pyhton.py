import math

class Feature:
    pass

class Polyline(Feature):
    def __init__(self, points=None):
        if points is None:
            self.points = []
        else:
            self.points = points

    def setPoints(self, points):
        self.points = points

    def getLength(self):
        length = 0.0
        for i in range(len(self.points) - 1):
            length += math.sqrt(
                (self.points[i].x - self.points[i + 1].x) ** 2 +
                (self.points[i].y - self.points[i + 1].y) ** 2
            )
        return length

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Туршилт
pt1 = Point(0, 0)
pt2 = Point(3, 4)
pt3 = Point(6, 4)

line = Polyline([pt1, pt2, pt3])
print("Polyline-ийн нийт урт:", line.getLength())
