import random


class Dice:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def roll(self):
        result1 = self.x
        result2 = self.y
        return result1, result2


dice = Dice(random.randint(1, 6), random.randint(1, 6))
roll = dice.roll()
print(roll)
