from Rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, f_side):
        if f_side <= 0:
            raise ValueError("Переданное значение меньше или равно нулю")
        self.f_side = f_side
        super().__init__(f_side, f_side)

