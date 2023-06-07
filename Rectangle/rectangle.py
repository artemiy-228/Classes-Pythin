class Rectangle:
    def __init__(self, length=2, width=2):
        self.length = length
        self.width = width
        self.area_v = self.area()

    def perimetеr(self):
        return (self.length + self.width) * 2

    def area(self):
        return self.width * self.length

    def display(self):
        print(f"Length of rectangle is {self.length}")
        print(f"Width of rectangle is {self.width}")
        print(f"Perimeter of rectangle is {self.perimetеr()}")
        print(f"Area of rectangle is {self.area_v}")
