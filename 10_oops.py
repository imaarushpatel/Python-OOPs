# Multi-level Inheritance

# Extend the Animal class with a subclass Mammal, and further extend Mammal with a subclass Human.
# Add methods in each class to display unique behavior.


class Animal:
    def uniqueBehaviour(self):
        print("Gandu Janwar")


class Mammal(Animal):
    def uniqueBehaviour(self):
        super().uniqueBehaviour()
        print("Chhoti Si Nanhi Si pyari")


class Human(Mammal):
    def uniqueBehaviour(self):
        super().uniqueBehaviour()
        print("Chutiya log and Selfish Behaviour")





human=Human()

human.uniqueBehaviour()

