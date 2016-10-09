import math

class Line(object):
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        d = ((x2-x1)**2+(y2-y1)**2)**0.5
        return d
    
    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        s = (y2-y1)/(x2-x1)

d = Line((0,0),(4,3))
print("d slope: " + str(d.slope()))

class Cylinder(object):
    
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        base = math.acos(-1) * (self.radius**2)
        vol = base * self.height
        return vol   

    def surface_area(self):
        base_perimeter = 2 * math.acos(-1) * self.radius
        base = math.acos(-1) * (self.radius**2)
        surface = base_perimeter*self.height + 2*base
        return surface

c = Cylinder()

print("volume: " + str(c.volume()))
print("surface: " + str(c.surface_area()))