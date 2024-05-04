from Circle import Circle
from Square import Square
from Rectangle import Rectangle
from Triangle import Triangle


def generate_figure(figure, *args):
    if figure == "circle":
        return Circle(args[0])
    elif figure == "square":
        return Square(args[0])
    elif figure == "rectangle":
        return Rectangle(args[0], args[1])
    elif figure == "triangle":
        return Triangle(args[0], args[1], args[2])
    else:
        raise ValueError