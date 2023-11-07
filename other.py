class Fruit:
    color = ""
    price = ""

sum here
    def __init__(self, color, price):  # Creating Constructor
        self.color = color
        self.price = price

    def print (self, a):



    # create method / function under fruit class
    def display(self):
        print(f"Color : {self.color}, Price : {self.price}")


# If we want to use the commmon properties/ variables that is defined in class we need to create Object

apple = Fruit("red", 2.4)  # create object; here apple is an object
# apple.color="Red"
# apple.price=2.4
# apple.set_Value("red",2.4)
apple.display()

Orange = Fruit("Orange", 1.99)  # create object; here Orange is an object
# Orange.color="Orange"
# Orange.price=0.9
Orange.display()

# print(f"Color : {apple.color}, Price : {apple.price}") # {placeholder/container/ variable}
# print(f"Color : {Orange.color}, Price : {Orange.price}")
# print(isinstance(apple, Fruit))   # Variable=> Instance, Property, Attrubute