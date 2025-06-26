# Implement Methods

# Add a method greet() to the Person class that prints a greeting message using the name attribute.




class Person:
    def __init__(self,name ,age):
        self.name=name
        self.age=age


    def greet(self):
        return f"Good Morning {self.name}"    


person1= Person("Rajan Patel" , 19)

# print(person1.name , person1.age)

print(person1.greet())
