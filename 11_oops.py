# Polymorphism


# Method Overloading (via Default Arguments)

# Create a class MathOperations with a method add() that can add two or three numbers (use default arguments).

class MathOperations:
    def add(self, a, b,c=0):
        return a+b+c
    


maths_ops=MathOperations()

print(maths_ops.add(2,4))
print(maths_ops.add(33,44,55))