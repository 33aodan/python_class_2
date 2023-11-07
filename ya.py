class Triangles:
    base = ""
    height = ""
    area = ""
    product = ""

    def __init__(self, base, height):
        self.base = base
        self.height = height
        self.product = self.base * self.height
        self.area = self.product / 2

    def display(self):
        print(f"Base : {self.base}, Height : {self.height}, Area : {self.area}")


triangle1 = Triangles(10, 20)
triangle1.display()
triangle2 = Triangles(20,30)
triangle2.display()
triangle3 = Triangles(30,40)
triangle3.display()
