# Simple Inheritance

# Create a base class Animal with a method make_sound().
# Create a subclass Dog that overrides the make_sound() method to print "Bark".

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

