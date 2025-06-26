# Abstract Class
# Create an abstract class Shape with a method area().
# Create subclasses Circle and Rectangle that implement the area() method.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass



class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius


    def area(self):
        return 3.14 * self.radius ** 2
    



class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length= length
        self.breadth=breadth



    def area(self):
        return self.length * self.breadth
    




cir=Circle(3)
rect=Rectangle(2,4)

print(cir.area())
print(rect.area())