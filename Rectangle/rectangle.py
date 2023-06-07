class Rectangle():
    def __init__(self, length=2, width=2):
        self.length = length
        self.width = width

    def Calc_Perimetеr(self):
        return (self.length + self.width) * 2

    def Calc_Area(self):
        return self.width * self.length

