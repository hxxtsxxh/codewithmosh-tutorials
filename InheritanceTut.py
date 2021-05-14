"""class Dog:
    def walk(self):
        print("walk")

class Cat:
    def walk(self):
        print("walk")"""


# INSTEAD, DO THIS

class Mammal:
    def __init__(self):
        pass


    def walk(self):
        print("walk")


class Dog(Mammal):  # ! This is called inheritance. This way, you don't repeat methods
    def bark(self):
        print("bark")


class Cat(Mammal):
    def be_annoying(self):
        print("annoying")


dog1 = Dog()
cat1 = Cat()
dog1.walk()
dog1.bark()
cat1.be_annoying()
cat1.walk()
