# Overload Operators

# Create a class Vector to represent a 2D vector with x and y coordinates.
# Overload the + operator to add two vectors.


class Vector:
    def __init__(self, x, y):
        self.x=x
        self.y=y



    def __add__(self,other):
        return Vector(self.x + other.x, self.y + other.y)
    


    def __str__(self):
      return f"Vector({self.x},{self.y})"



v1 = Vector(2, 6)
v2 = Vector(3, 4)
v3 = v1 + v2

print(v3)