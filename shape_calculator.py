

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
        
    def get_amount_inside(self,shape=0):
        #the returned amount of rectangles or squares should be integer
        #if its a rectangle
        if shape == self:
            #if the hheight of the rectanle is an odd number
            if self.height % 2 != 0:
                return 0
            else:
                return int(self.get_area()/(self.get_perimeter()/2))
        elif shape == 0:
            return int(self.get_area()/(self.get_perimeter()/2))
        else:
            print("this is a defined square")
            return int(self.get_area()/shape.get_perimeter())
    
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

rect = Rectangle(15, 10)
print(rect.get_picture())
print(rect.get_amount_inside())



