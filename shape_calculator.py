class Rectangle:
    object_list= []
    def __init__(self,width=int(),height=int()):
        self.width = width
        self.height = height
        Rectangle.object_list.append(self)
    
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
    
    def get_amount_inside(self,object):
        if not object in Rectangle.object_list:
            return f"{object} is not an object"
        else:
            return self.get_area()/object.sides
    
    def __repr__(self):
        return f"{self.__class__.__name__}(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side_length):
        self.width = side_length
        self.height = side_length
        Rectangle.object_list.append(self)
    
    def set_side(self,sides=str()):
        self.sides = sides
        self.width = sides
        self.height = sides    

    def __repr__(self):
        return f"{self.__class__.__name__}(sides={self.sides})"


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(Rectangle.object_list)
print(rect.get_amount_inside(sq))