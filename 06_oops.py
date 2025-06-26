# Create a Class and Object

# Define a class Person with attributes name and age.
# Create an object of the class and print its attributes.


class Person:
    def __init__(self,name ,age):
        self.name=name
        self.age=age


# name = "Rajan"
# age=19


# person1= Person(f"My name is {name}", f"I am {age} yers old")

person1= Person("Rajan Patel" , 19)

print(person1.name , person1.age)
