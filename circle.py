from math import pi, sqrt


class Circle:

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius


    def area(self):
        return pi * self.radius ** 2


    def perimeter(self):
        return pi * 2 * self.radius


    def test_belongs(self, a, b):
        distance = sqrt((self.x - a)**2 + (self.y - b)**2)
        return distance <= self.radius


    def display(self):
        print(f"Circle radius is {self.radius}")
        print(f"Circle area is {self.area()}")
        print(f"Circle perimeter is {self.perimeter()}")


circle = Circle(0, 0, 10)
circle.display()
print(circle.test_belongs(5, 5))
print(circle.test_belongs(10, 10))