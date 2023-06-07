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
        print(f"Length is {self.length} units")
        print(f"Width is {self.width} units")
        print(f"Perimeter is {self.perimetеr()} units")
        print(f"Area is {self.area_v} units")

class Parallelepipede(Rectangle):

    def __init__(self, length=3, width=4, height=5):
        Rectangle.__init__(self, length, width)
        self.height = height

    def volume(self):
        return Rectangle.area(self) * self.height

    def display(self):
        Rectangle.display(self)
        print(f"Volume is {self.volume()} units")


print("Rectangle: ")
Rect = Rectangle(5, 6)
Rect.display()
print("Parallelepipede: ")
Parall = Parallelepipede(6, 8, 7)
Parall.display()