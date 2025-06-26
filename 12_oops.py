# Method Overriding

# Use the Animal and Dog classes from the inheritance example.
# Call make_sound() from both the base class and subclass objects.



class Animal:
    def make_sound(self):
        print("BHOWW BHOWWW")



class Dog(Animal):
    def make_sound(self):
        print("Bark")


animal=Animal()
dog=Dog()

animal.make_sound()
dog.make_sound()

