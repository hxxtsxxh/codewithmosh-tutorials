import turtle

cute_turtle = turtle.Turtle()


def square():
    cute_turtle.speed(2)
    cute_turtle.color('blue')
    cute_turtle.forward(100)
    cute_turtle.right(90)
    cute_turtle.forward(100)
    cute_turtle.right(90)
    cute_turtle.forward(100)
    cute_turtle.right(90)
    cute_turtle.forward(100)
    cute_turtle.color('blue')
    cute_turtle.clone()
    cute_turtle.speed(2)


for i in range(4):
    square()
    print(i)

start = True
while start:
    exit_func = input('Do you want to quit? (Press Q) ')
    if exit_func.upper() == 'Q':
        start = False
    else:
        print('Please type Q')
        continue
