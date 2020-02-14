'''
Created on Feb 13, 2020

@author: zhangwei
'''

class Shape:
    def __init__(self, area, perimeter):
        self.area = area
        self.perimeter = perimeter
    def getArea(self):
        return self.area
    def getPerimeter(self):
        return self.perimeter
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        self.area = 3.14 * self.radius * self.radius
        self.perimeter = 2 * 3.14 * self.radius
        
class Square(Shape):
    def __init__(self, side):
        self.side = side
        self.area = self.side * self.side
        self.perimeter = 4 * side
    
c = Circle(5)
s = Square(5)
print(c.getArea())
print(s.getArea())