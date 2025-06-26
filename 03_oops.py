#INheritance

class Car:
    def __init__(self, brand, model):
        self.brand=brand
        self.model=model

    def fullname(self):
        return  f"{self.brand} {self.model} {self.battery_size}"
    


class ElectricCar(Car): 
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size=battery_size  




my_car= ElectricCar("Tesla", "Model S", "5000kw")

print(my_car.model)   
print(my_car.fullname()) 