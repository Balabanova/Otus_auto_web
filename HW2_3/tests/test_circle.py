import pytest
from Circle import Circle
from figure_generation import generate_figure


def instance_circle(result, radius):
    if not result:
        with pytest.raises(Exception):
            Circle(radius=radius)
        return "OK"
    else:
        c = Circle(radius=radius)
        return c


@pytest.mark.parametrize("inst_circ, area, perim",
                         [(instance_circle(True, 1), 3.142, 6.283),
                          (instance_circle(False, 0), "Null", "Null"),
                          (instance_circle(False, -1), "Null", "Null"),
                          (instance_circle(True, 1.1), 3.801, 6.912)], ids=["integer", "0", "negative", "float"])
class TestCircle:

    def test_circle_area(self, inst_circ, area, perim):
        if inst_circ == "OK":
            pass
        else:
            assert inst_circ.area == area

    def test_circle_perimeter(self, inst_circ, area, perim):
        if inst_circ == "OK":
            pass
        else:
            assert inst_circ.perimeter == perim


@pytest.mark.parametrize("figure, result, sum",
                         [(generate_figure("circle", 7), True, 166.504),
                          (generate_figure("square", 7), True, 61.566),
                          (generate_figure("rectangle", 7, 4), True, 40.566),
                          (generate_figure("triangle", 11, 12, 13), True, 74.048),
                          (15, False, 166.504)], ids=["circle", "square", "rectangle", "triangle", "not_figure"])
class TestFigure:
    def test_add_figure(self, figure, result, sum):
        c = Circle(radius=2)
        if not result:
            with pytest.raises(Exception):
                c.add_area(figure)
        else:
            res = c.add_area(figure)
            assert res == sum
