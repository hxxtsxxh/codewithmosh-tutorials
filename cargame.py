car_start = "Car started..Ready to go"
car = 'I am a car'
car_stop = "Car stopped."
quit_game = "Bye!"
help_game = '''
start: starts the car
stop: stops the car
quit: exits game
'''

car_game = True
started = False
while car_game:
    main = input("> ")
    if main == "help":
        print(help_game)
    elif main == "start":
        if started:
            print("Car is already started.")
        else:
            started = True
            print(car_start)
    elif main == "stop":
        if not started:
            print("Car is already stopped.")
        else:
            started = False
            print(car_stop)
    elif main == "quit":
        print(quit_game)
        break
    else:
        print("Error: type valid input")
