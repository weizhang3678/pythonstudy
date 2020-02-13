'''
Created on Feb 13, 2020

@author: zhangwei
'''
# same method, different behavior

class Triangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def getArea(self):
        area = self.height * self.width /2.0
        return area
        
class Square:
    def __init__(self,side):
        self.side = side
        
    def getArea(self):
        return self.side * self.side
    
t = Triangle(4,5)
print(str(t.getArea()))

s = Square(5)
print(str(s.getArea()))
        