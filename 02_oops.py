class Car:
    def __init__(self, brand, model):
        self.brand=brand
        self.model=model

    def fullname(self):
        return  f"{self.brand} {self.model}"




my_car= Car("Suziki", "Desire")

print(my_car.fullname())    #note: when we are going to print functanality we use () exp. in fulname as it is function but we have a variable we direrctly print that like model and brand