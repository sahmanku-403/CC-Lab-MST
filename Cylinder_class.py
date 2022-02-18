class Cylinder:
    def __init__(self, height= 1, radius =1):
        self.height = height
        self.radius = radius
    def volume(self):
        return round(3.14*self.radius*self.radius*self.height,2)
    def surface_area(self):
        return 2*3.14*self.radius*(self.height+self.radius)
    
