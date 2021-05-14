weight_input = int(input("Weight: "))
ask_format = input("(L)bs or (K)g: ")
if ask_format.upper() == 'L':
    conversion = weight_input / 2.205
    print(f"{round(conversion)} kg")
elif ask_format.upper() == 'K':
    conversion = weight_input * 2.205
    print(f"{round(conversion)} lbs")
else:
    print("ERROR: Print valid input!")
