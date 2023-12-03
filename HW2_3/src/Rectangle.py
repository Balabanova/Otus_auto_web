from Figure import Figure


class Rectangle(Figure):

    def __init__(self, s_side, f_side):
        if s_side <= 0 or f_side <= 0:
            raise ValueError("Переданное значение меньше или равно нулю")

        self.f_side = f_side
        self.s_side = s_side
        self.area = self.find_area()
        self.perimeter = self.find_perimeter()

    def find_perimeter(self):
        return round((self.f_side + self.s_side) * 2, 3)

    def find_area(self):
        return round(self.f_side * self.s_side, 3)
