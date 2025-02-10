# Constructors and Class Methods

# __init__ method: it runs as soon as an object of a class is instantiated
class MyClass:
    def __init__(self, name):
        self.name = name
        print(f"Welcome to {self.name}.")

my_class = MyClass("Favelas")

# other method
class MyClass:
    def __init__(self, name):
        self.name = name
        print(f"Welcome to {self.name}.")

    def my_method(self, number):
        print(f"The cube of number {number} is {number**3}.")

print()
my_class = MyClass("Cube calculator")
my_class.my_method(number = 3)
