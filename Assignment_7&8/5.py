# Create a base class "Shape" with methods to calculate the area and perimeter. Implement
# derived classes "Rectangle" and "Circle" that inherit from "Shape" and provide their own area
# and perimeter calculations.

from abc import abstractmethod
from typing import List

class Shape:
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass
    
class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)
    
    def perimeter(self):
        return 2 * 3.14 * self.radius
    
class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width
        
    def area(self):
        return super().area()
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
obj1 = Circle(5)
obj2 = Rectangle(5, 3)

print(obj1.area())
print(obj1.perimeter())
print(obj2.area())
print(obj2.perimeter())