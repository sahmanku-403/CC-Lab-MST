#Program to implement basic complex number arithmetic

#the arithmetic operations implemented:
#addition, substaction, multiplication, division, reciprocal

class Complex:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return f'{self.x}+i{self.y}'
    #we shall define the operations now

    def add(this, complex2):
        return Complex(this.x+complex2.x, this.y+complex2.y)

        
   


    def subtract(this, complex2):
        #Subtract here and return object
        return Complex(this.x-complex2.x, this.y-complex2.y)
    def multiply(this, complex2):
        return Complex(this.x*complex2.x-this.y*complex2.y, this.x*complex2.y+this.y*complex2.x)
        #Multiply here and return object
    def reciprocal(this):
        if(this.x == 0 and this.y == 0):
            raise ZeroDivisionError("Attempt to divide by zero")
        r = this.x**2+this.y**2
        return Complex(this.x/r, -this.y/r)
        
        #reciprocal here and return object
    def divide(this, complex2):
        return this.multiply(complex2.reciprocal());
        #divide here and return object
