class Line(object):

    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
    	x1,y1 = self.coor1
    	x2,y2 = self.coor2
        print ((x2-x1)**2 + (y2-y1)**2 )**0.5
    
    def slope(self):
    	x1,y1 = self.coor1
    	x2,y2 = self.coor2
        print float(y2-y1)/(x2-x1)


class Cylinder(object):
    pi = 3.14
    def __init__(self,height=1,radius=1):
        self.radius = radius
        self.height = height
        
    def volume(self):
        print Cylinder.pi*self.radius**2*self.height
    
    def surface_area(self):
        print 2*Cylinder.pi*self.radius*self.height + 2*Cylinder.pi*self.radius**2

c = Cylinder(2,3)
c.volume()
c.surface_area()

coordinate1 = (3,2)
coordinate2 = (8,10)


li  = Line(coordinate1,coordinate2)

li.distance()
li.slope()