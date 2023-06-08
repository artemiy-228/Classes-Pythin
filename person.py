class Person:

    def __init__(self, name="Student", age=18):
        self.age = age
        self.name = name


    def display(self):
        print(f"Student {self.name} is {self.age} years old")

