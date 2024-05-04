import pytest
from Square import Square
from figure_generation import generate_figure


def instance_square(result, side):
    if not result:
        with pytest.raises(Exception):
            Square(f_side=side)
        return "OK"
    else:
        s = Square(f_side=side)
        return s


@pytest.mark.parametrize("inst_sq, area, perim",
                         [(instance_square(True, 1), 1, 4),
                          (instance_square(False, 0), "Null", "Null"),
                          (instance_square(False, -1), "Null", "Null"),
                          (instance_square(True, 1.1), 1.21, 4.4)], ids=["integer", "0", "negative", "float"])
class TestSquare:

    def test_square_area(self, inst_sq, area, perim):
        if inst_sq == "OK":
            pass
        else:
            assert inst_sq.area == area

    def test_square_perimeter(self, inst_sq, area, perim):
        if inst_sq == "OK":
            pass
        else:
            assert inst_sq.perimeter == perim


@pytest.mark.parametrize("figure, result, sum",
                         [(generate_figure("circle", 7), True, 157.938),
                          (generate_figure("square", 7), True, 53),
                          (generate_figure("rectangle", 7, 4), True, 32),
                          (generate_figure("triangle", 11, 12, 13), True, 65.482),
                          (15, False, "None")], ids=["circle", "square", "rectangle", "triangle", "not_figure"])
class TestFigure:
    def test_add_figure(self, figure, result, sum):
        s = Square(2)
        if not result:
            with pytest.raises(Exception):
                s.add_area(figure)
        else:
            res = s.add_area(figure)
            assert res == sum
