from Figure import Figure
import math


class Circle(Figure):

    def __init__(self, radius):
        self.radius = radius
        self.perimeter = self.find_perimeter()
        self.area = self.find_area()

    def find_perimeter(self):
        return round(2 * math.pi * self.radius, 3)

    def find_area(self):
        return round(math.pi * (self.radius**2), 3)


