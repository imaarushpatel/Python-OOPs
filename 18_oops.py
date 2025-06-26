# School Management

# Create a Person class for students and teachers.
# Add methods to display details and calculate grades or salaries based on input.


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age


    def show_details(self):
        print(f"Name:{self.name}, Age:{self.age}")


class Students(Person):
    def __init__(self, name, age,student_id,grade):
        super().__init__(name, age)
        self.student_id=student_id
        self.grade=grade


    def show_details(self):
            super().show_details()
            print(f"Student ID: {self.student_id}, Grade:{self.grade}")



class Teachers(Person):
    def __init__(self, name, age, subject, salary):
        super().__init__(name, age)
        self.subject=subject  
        self.salary=salary\
        

    def show_details(self):
        super().show_details()
        print(f"Subject:{self.subject}, Salary:{self.salary}")




student=Students("Khushi",21, 11,"A++",)
teacher=Teachers("Rajan",21,"Biology", 14300)



print("Student Details:")
student.show_details() 


print("\nTeacher Details:")
teacher.show_details()