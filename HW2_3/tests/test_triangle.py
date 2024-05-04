import pytest
from Triangle import Triangle
from figure_generation import generate_figure


def instance_rectangle(result, side_a, side_b, side_c):
    if not result:
        with pytest.raises(Exception):
            Triangle(f_side=side_a, s_side=side_b, t_side=side_c)
        return "OK"
    else:
        r = Triangle(f_side=side_a, s_side=side_b, t_side=side_c)
        return r


@pytest.mark.parametrize("inst_tr, area, perim",
                         [(instance_rectangle(True, 11, 12, 13), 61.482, 36),
                          (instance_rectangle(False, 0, 1, 2), "Null", "Null"),
                          (instance_rectangle(False, -1, 1, 1), "Null", "Null"),
                          (instance_rectangle(True, 11.1, 12.1, 13.1), 62.525, 36.3),
                          (instance_rectangle(False, 1, 2, 1), "Null", "Null")],
                         ids=["integer", "0", "negative", "float", "nonexistent"])
class TestTriangle:

    def test_instance_rectangle_area(self, inst_tr, area, perim):
        if inst_tr == "OK":
            pass
        else:
            assert inst_tr.area == area

    def test_instance_rectangle_perimeter(self, inst_tr, area, perim):
        if inst_tr == "OK":
            pass
        else:
            assert inst_tr.perimeter == perim


@pytest.mark.parametrize("figure, result, sum",
                         [(generate_figure("circle", 7), True, 206.333),
                          (generate_figure("square", 7), True, 101.395),
                          (generate_figure("rectangle", 7, 4), True, 80.395),
                          (generate_figure("triangle", 11, 12, 13), True, 113.877),
                          (15, False, "None")], ids=["circle", "square", "rectangle", "triangle", "not_figure"])
class TestFigure:
    def test_add_figure(self, figure, result, sum):
        t = Triangle(11, 11, 11)
        if not result:
            with pytest.raises(Exception):
                t.add_area(figure)
        else:
            res = t.add_area(figure)
            assert res == sum
