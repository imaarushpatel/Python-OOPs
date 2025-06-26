# Employee Management

# Create a base class Employee with attributes name and salary.
# Add a subclass Manager with an additional attribute department.
# Add methods to calculate bonuses based on salary.


class Employee:
    def __init__(self, name , sallary):
        self.name=name
        self.sallary=sallary



    def calc_bonus(self):
        return self.sallary * 0.1
    

class Manager(Employee):
    def __init__(self,name,sallary,department):
        super().__init__(name, sallary)
        self.department= department



        def calc_bonus(self):
            return  self.sallary * 0.2
        

emp= Employee("Rajan",50000)
mgr=Manager("Elon Musk", 60000, "Space")


print(emp.calc_bonus())
print(mgr.calc_bonus())



