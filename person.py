class Person:

    def __init__(self, name="Person", age=30):
        self.age = age
        self.name = name


    def display(self):
        print(f"Student {self.name} is {self.age} years old")



class Student(Person):

    def __init__(self, name="Student", age=18, major="Math"):
        Person.__init__(self, name, age)
        self.major = major


    def display_student(self):
        Person.display(self)
        print(f"{self.name} has {self.major} major")


Artem = Student(name="Artem", age=18, major="Programming")

Artem.display_student()