# Method overloading and overriding

# Method overloading allows to define two methods with the same name but different parameters. The right method will be chosen based on 
# the passed parameters. Python DOES NOT support method overloading. 

class Rabbit:
    def eat(self):
        print("Eating celery.")
    def eat(self, food):
        print(f"Eating {food}.")

rabbit = Rabbit()
# rabbit.eat() # Error
rabbit.eat(food="fennel") # Output: "Eating fennel". The last method overwrite the former

# Method overriding: allow to overwrite the parent class method. This is useful when you want the child's method to have special
# functionalities.

class Rabbit: 
    def eat(self):
        print("Eating celery.")

class HungryRabbit(Rabbit):
    def eat(self): # this overwrite the previous method
        print("Eating celery fast.")

hungry_rabbit = HungryRabbit()
hungry_rabbit.eat() 