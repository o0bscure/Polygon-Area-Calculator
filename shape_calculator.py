from cmath import rect


class Rectangle:
    
    def __init__(self,width,height):
        self.width = width
        self.height = height
    
    def set_width(self):
        pass
    
    def set_height(self):
        pass
    
    def get_area(self):
        return self.width * self.height
        





    class Square:
        pass


rect = Rectangle(3,6)
print(type(rect))