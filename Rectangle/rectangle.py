class Rectangle():

    def __init__(self, length=2, width=2):
        self.length = length
        self.width = width

    def Calc_Perimetеr(self):
        print(f"Perimetеr of Rectangle is {(self.length + self.width) * 2} units")

    def Calc_Area(self):
        print(f"Area of Rectangle is {self.width * self.length} square units")

