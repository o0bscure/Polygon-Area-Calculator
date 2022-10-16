from turtle import width
from unittest import result


class Rectangle:
    def __init__(self,width=int(),height=int()):
        self.width = width
        self.height = height
    
    def set_width(self,width=int()):
        self.width = width
    
    def set_height(self,height=int()):
        self.height = height
    
    def get_area(self):
        return self.width * self.height
        
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
    
    def get_picture(self):
        marker = self.width * "*"
        lines = self.height
        result = ""
        for line in range(lines):
            result = result + marker + "\n"
        return result
    
    def __str__(self):
        return f"{self.__class__.__name__}(width={self.width}, height={self.height})"


class Square(Rectangle):
    def set_side(self,sides=str()):
        self.sides = sides    

    def __str__(self):
        return f"{self.__class__.__name__}(sides={self.sides})"


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(10,9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

#rect.set_height(8)
#rect.set_width(16)
#print(rect.get_amount_inside(sq))