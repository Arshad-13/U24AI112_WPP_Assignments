# Create a class for representing any 2-D point or vector. The methods inside this class include
# its magnitude and its rotation with respect to the X-axis. Using the objects define functions for
# calculating the distance between two vectors, dot product, cross product of two vectors. Extend
# the 2-D vectors into 3-D using the concept of inheritance. Update the methods according to 3-
# D.
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

    def rotate(self, angle):
        x = self.x * math.cos(angle) - self.y * math.sin(angle)
        y = self.x * math.sin(angle) + self.y * math.cos(angle)
        return Point(x, y)

    def distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
    
class TwoDVector(Point):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def rotate(self, angle):
        x = self.x * math.cos(angle) - self.y * math.sin(angle)
        y = self.x * math.sin(angle) + self.y * math.cos(angle)
        return TwoDVector(x, y, self.z)
    
    def distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2)
    
    def dot_product(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def cross_product(self, other):
        x = self.y * other.z - other.y * self.z
        y = self.x * other.z - other.x * self.z
        z = self.x * other.y - other.x * self.y
        return x,y,z
    
v1 = TwoDVector(1, 2, 0)
v2 = TwoDVector(4, 5, 0)
print(v1.magnitude())
a,b,c = v1.rotate(math.pi/2).x, v1.rotate(math.pi/2).y, v1.rotate(math.pi/2).z
print(a,b,c)
print(v1.distance(v2))
print(v1.dot_product(v2))
a,b,c = v1.cross_product(v2)
print(a,b,c)