def square(number):
    return number * number


answer = square(int(input('type a number\n')))
print(answer)

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


print('Hello this is your calculator! \n')
ask = input('''Pick from the following
1) Add
2) Subtract
3) Multiply
4) Divide\n''')

answer_choice1 = ['Add', 1]
answer_choice2 = ['Subtract', 2]
answer_choice23 = ['Multiply', 3]
answer_choice4 = ['Divide', 4]

if ask in answer_choice1:
    print()
