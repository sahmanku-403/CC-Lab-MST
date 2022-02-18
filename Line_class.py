class Line:
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    def distance(self):
        a =(coor1[0]-coor2[0])**2
        b =(coor1[1]-coor2[1])**2
        return (a+b)**0.5
    def slope(self):
        x = coor2[0]-coor1[0]
        y = coor2[1]-coor1[1]
        return y/x
