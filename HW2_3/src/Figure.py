from abc import ABC, abstractmethod


class Figure(ABC):

    @abstractmethod
    def find_perimeter(self):
        pass

    @abstractmethod
    def find_area(self):
        pass

    def add_area(self, s_figure):
        if isinstance(s_figure, Figure):
            return round(float(self.area) + float(s_figure.area), 3)
        else:
            raise ValueError("Передана не фигура")






