"""
class Point:
    def __init__(self, x, y): #!this method is a constructor.
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point = Point(10, 20)
print(point.x)

"""


# EXERCISE - create a Person class, and then have a name attribute along with a talk method

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")


person = Person("Heet Shah")
person.talk()

person2 = Person("Bob Smith")
person2.talk()

person3 = Person("Ekta Shah")
person3.talk()
