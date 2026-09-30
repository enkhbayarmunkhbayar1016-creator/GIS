import math

class Feature:
    pass

class Polyline(Feature):
    def __init__(self, points = []):
        self.points = points
        
   
    def setPoints(self, points):
        self.points = points
        
    
    def getLength(self):
        length = 0.0
        for i in range(len(self.points)-1):
            length+=math.sqrt((self.points[i].x-self.points[i+1].x)**2+(self.points[i].y-self.points[i+1].y)**2)
            
        return length