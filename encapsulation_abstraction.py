# Abstraction, Encapsulation, Data Hiding

# Abstraction is used to hide the irrelevant data/class in order to reduce the complexity
# and it also enhances the application efficency. Abstraction classes are meant to be the blueprint
# of the other classes.
from abc import ABC # module for abstraction in Python 
class Animal(ABC):
    def get_sound(self):
        pass

class Cow(Animal):
    def get_sound(self):
        print("Moooo")

print("# 1")
cow = Cow()
cow.get_sound()

# Encapsulation is the process of wrapping up variables and methods into a single entity. It
# can prevent accidental or unauthorized modification of data. 
# Python does not have the "private" keyword, but is based on conventions:
# - a class variable that should not directly be accessed should be prefixed with an underscore
    # - _single underscore: private variable, it should not be accessed directly 
    # - __double underscore: private variable, harder to access but still possible
class Rabbit():
    def __init__(self):
        self.name = "Giovanna"
        self._num_ears = 2
        self.__owner = "Alex"

rabbit = Rabbit()
print("\n# 2")
print(rabbit.name)
print(rabbit._num_ears)
print(rabbit.__owner) # Error

# To show the encapsulated value use the following syntax (name mangling): 
print(rabbit._Rabbit__owner)