# Create python classes
class MyClass:
    "This is a docstring."
    var = 19
    def fun():
        print("Hello, this is a class function.")

print("\n# 1")
print(MyClass.__doc__)
print(MyClass.var)
MyClass.fun()

# Instantiate an object
my_class = MyClass()
print("\n# 2")
print(my_class.__doc__)
print(my_class.var)
# my_class.fun() # Error! We need to introduce the self parameter 

class MyClass2:
    "This is a docstring."
    var = 19
    def fun(self):
        print("Hello, this is a class function.")

my_class_2 = MyClass2()
print("\n# 3")
print(my_class_2.__doc__)
print(my_class_2.var)
my_class_2.fun()