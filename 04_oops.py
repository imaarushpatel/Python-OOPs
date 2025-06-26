#Encapsulation 


class Person:
    def __init__(self, name, age):
        self.name = name          # Public attribute
        self.__age = age          # Private attribute (encapsulation)

    # Getter method to access private attribute
    def get_age(self):
        return self.__age

    # Setter method to modify private attribute
    def set_age(self, age):
        if age > 0:               # Adding a condition to ensure valid age
            self.__age = age
        else:
            print("Age must be positive!")

# Using the class
person = Person("Alice", 25)

# Accessing public attribute
print(person.name)  # Output: Alice

# Trying to access private attribute directly (will cause an error)
# print(person.__age)  # AttributeError: 'Person' object has no attribute '__age'

# Accessing private attribute using getter
print(person.get_age())  # Output: 25

# Modifying private attribute using setter
person.set_age(30)
print(person.get_age())  # Output: 30

# Invalid age input
person.set_age(-5)       # Output: Age must be positive!
