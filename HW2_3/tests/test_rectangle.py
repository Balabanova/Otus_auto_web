import pytest
from Rectangle import Rectangle
from figure_generation import generate_figure


def instance_rectangle(result, side_a, side_b):
    if not result:
        with pytest.raises(Exception):
            Rectangle(f_side=side_a, s_side=side_b)
        return "OK"
    else:
        r = Rectangle(f_side=side_a, s_side=side_b)
        return r


@pytest.mark.parametrize("inst_rec, area, perim",
                         [(instance_rectangle(True, 1, 2), 2, 6),
                          (instance_rectangle(False, 0, 1), "Null", "Null"),
                          (instance_rectangle(False, -1, 1), "Null", "Null"),
                          (instance_rectangle(True, 1.1, 2.2), 2.42, 6.6)], ids=["integer", "0", "negative", "float"])
class TestRectangle:

    def test_instance_rectangle_area(self, inst_rec, area, perim):
        if inst_rec == "OK":
            pass
        else:
            assert inst_rec.area == area

    def test_instance_rectangle_perimeter(self, inst_rec, area, perim):
        if inst_rec == "OK":
            pass
        else:
            assert inst_rec.perimeter == perim


@pytest.mark.parametrize("figure, result, sum",
                         [(generate_figure("circle", 7), True, 163.938),
                          (generate_figure("square", 7), True, 59),
                          (generate_figure("rectangle", 7, 4), True, 38),
                          (generate_figure("triangle", 11, 12, 13), True, 71.482),
                          (15, False, "None")], ids=["circle", "square", "rectangle", "triangle", "not_figure"])
class TestFigure:
    def test_add_figure(self, figure, result, sum):
        r = Rectangle(2, 5)
        if not result:
            with pytest.raises(Exception):
                r.add_area(figure)
        else:
            res = r.add_area(figure)
            assert res == sum
