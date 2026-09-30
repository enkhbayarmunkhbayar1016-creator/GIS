import math

class Point:
    def __init__(self):
        #
        self.x = 0
        self.y = 0

    def setXY(self, x, y):

        self.x = x
        self.y = y

    def calDis(self, p):
       
        return math.sqrt((self.x - p.x)**2 + (self.y - p.y)**2)

# Туршилт:
p1 = Point()
p2 = Point()

p1.setXY(1, 2)
p2.setXY(2, 3)

distance = p1.calDis(p2)
print("1.7")
print("p1 and p2 result", distance)