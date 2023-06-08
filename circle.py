from math import pi


class Circle:

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return pi * 2 * self.radius
