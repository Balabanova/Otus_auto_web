from Rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, f_side):
        if f_side >= 0 or f_side.isdigit():
            self.f_side = f_side
        else:
            raise ValueError("Переданное значение меньше нуля")
        super().__init__(f_side, f_side)

