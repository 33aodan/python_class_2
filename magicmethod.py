# class student:
#     def __init__(self, name, id):
#         self.name=name
#         self.id=id
#
#     def __str__(self):
#         return (f"name: {self.name}, ID: {self.id}")
#
#     def display(self):
#         print(f"{self.name},{self.id}")
#
# student1 = student("name",234)
# student2 = student("peepee",112)
#
# print(student1)

class addition:
    def __init__(self, num1):
        self.num1 = num1
    def __add__(self,other):
        return addition(self.num1 + other.num1)

Num1 = addition(3)
Num2 = addition(5)
Sum = Num1+Num2
print(Sum.num1)