from abc import ABC, abstractmethod
class Shape(ABC):
    product = ""
    area2 = ""

    def __init__(self, dim1, dim2):
        self.dim1 = dim1
        self.dim2 = dim2

    @abstractmethod
    def area(self):
        pass


class Triangle(Shape):
    dim1 = ""
    dim2 = ""

    def area(self):
        product = self.dim1 * self.dim2
        area2 = product / 2
        print(area2)


class Rectangle(Shape):
    dim1 = ""
    dim2 = ""

    def area(self):
        area2 = self.dim1 * self.dim2
        print(area2)


tri = Triangle(2, 10)
tri.area()
rect = Rectangle(4, 5)
rect.area()
