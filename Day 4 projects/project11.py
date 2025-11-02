import math

class Shape:
    def get_area(self):
        
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return self.side ** 2

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2


square = Square(5)
circle = Circle(3)

print("Area of Square:", square.get_area())
print("Area of Circle:", circle.get_area())
