# Create a Class

class MyClass: # Usually class name starts with capital letter
    x = 5
    pass

p1 = MyClass()
print(p1.x)

# Adding attributes to the class (outside the class)
p1.name = "John"
print(p1.name)

# Init Class / Constructor Method
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.followers = 0 # Default value

p2 = Person("John", 36)
print(p2.name)
print(p2.followers)