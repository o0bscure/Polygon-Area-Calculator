from turtle import width


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
        return self
    
    def __str__(self):
        pass





    class Square:
        pass


rect = Rectangle()
print(type(rect))