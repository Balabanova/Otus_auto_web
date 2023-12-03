from Figure import Figure
import math


class Triangle(Figure):

    def __init__(self, f_side, s_side, t_side):
        if f_side < 0 or s_side < 0 or t_side < 0:
            raise ValueError("Переданное значение меньше нуля")
        if f_side + s_side <= t_side or f_side + t_side <= s_side or s_side + t_side <= f_side:
            raise ValueError("Невозможно создать треугольник с переданными сторонами")

        self.f_side = f_side
        self.s_side = s_side
        self.t_side = t_side
        self.perimeter = self.find_perimeter()
        self.area = self.find_area()

    def find_perimeter(self):
        self.perimeter = self.f_side + self.s_side + self.t_side
        return self.perimeter

    def find_area(self):
        p = self.perimeter / 2
        return round(math.sqrt((p * (p - self.f_side) * (p - self.s_side) * (p - self.t_side))), 3)
