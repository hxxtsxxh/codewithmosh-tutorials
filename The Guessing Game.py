import random
import time

failMessage = "Oops. You didn't get the right answer in any of the three chances."
secretNumber = random.randint(0, 10)
i = 0

win = False

while i < 3:
    guessNumber = int(input("Guess: "))
    if guessNumber == secretNumber:
        print("You win!")
        break
    else:
        print('Guess again.')
        i += 1
        time.sleep(0.5)

        if i == 3:
            print(f"GAME OVER: {failMessage}")
