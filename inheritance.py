# Inheritance in Python


# Single inheritance
class Animal:
    def __init__(self, name):
        print(f"Animal named {name}")
    def speak(self):
        print("Animal speaking.")

class Rabbit(Animal):
    def __init__(self): # if I add another contructor, this overwrite the previous from Animal. 
        pass

    def eat_celery(self):
        print("Rabbit eating celery.")

print("# 1")
rabbit = Rabbit()
rabbit.speak()
rabbit.eat_celery()



# Multilevel inheritance
# In inheritance, the child class acquirest the properties and can access all the data members and functions defined in the parent class
class Animal:
    def __init__(self, name):
        print(f"Animal named {name}")
    def speak(self):
        print("Animal speaking.")

class Rabbit(Animal):
    def __init__(self): # if I add another contructor, this overwrite the previous from Animal. 
        pass

    def eat_celery(self):
        print("Rabbit eating celery.")

# NO! Because Rabbit already inherits from Animal
# class MiniLop(Animal, Rabbit):
#     def stride_ears_on_the_floor(self):
#         print("Minilop striding ears on the floor.")

# Correct: 
class MiniLop(Rabbit):
    def stride_ears_on_the_floor(self):
        print("Minilop striding ears on the floor.")

animal = Animal(name="Giovanna")
rabbit = Rabbit()
minilop = MiniLop()

print("\n# 2")
print("Animal: ")
animal.speak()

print("Rabbit: ")
rabbit.speak()
rabbit.eat_celery()

print("Minilop: ")
minilop.speak()
minilop.eat_celery()
minilop.stride_ears_on_the_floor()



# Multiple inheritance 
class Animal:
    def __init__(self, name):
        print(f"Animal named {name}")
    def speak(self):
        print("Animal speaking.")

class GrayEntity:
    def be_gray(self):
        print(f"Gray entity being gray.")

class Rabbit(Animal, GrayEntity):
    def eat_celery(self):
        print("Rabbit eating celery.")

animal = Animal("Giovanna")
gray_entity = GrayEntity()
rabbit = Rabbit("Giovanna")

print("\n# 3")
rabbit.speak()
rabbit.be_gray()
rabbit.eat_celery()