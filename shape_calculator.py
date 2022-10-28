

class Rectangle:
    sides = int()
    def __init__(self,width=int(),height=int()):
        self.width = width
        self.height = height
    
    def set_width(self,width=int()):
        self.width = width
        self.sides = width
    
    def set_height(self,height=int()):
        self.height = height
        self.sides = height
    
    def get_area(self):
        return self.width * self.height
        
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:   
            marker = self.width * "*"
            lines = self.height
            result = ""
            for line in range(lines):
                result = result + marker + "\n"
            return result
    
    #calculate how many shapes can fit inside a rectangle   
    def get_amount_inside(self,shape=0):
        #checks if that sheo is a rectangle
        if self == shape:
            if self.height % 2 != 0:
                return 0
            elif self.height <= 8 and self.width <= 4:
                return 1
            else:
                return int(self.get_area()/(self.get_perimeter()/2))
        else:
            return int(self.get_area()/shape.get_perimeter())

    #string representation of the object
    def __repr__(self):
        return f"{self.__class__.__name__}(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side_length):
        self.width = side_length
        self.height = side_length
        self.sides = side_length
    
    def set_side(self,sides=str()):
        self.sides = sides
        self.width = sides
        self.height = sides    

    def __repr__(self):
        return f"{self.__class__.__name__}(side={self.sides})"

rect =Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq =Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))