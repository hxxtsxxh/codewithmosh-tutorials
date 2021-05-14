
running = True
while running:
    # this gets the input of the user's phone number.
    phone_number = input("Phone: ")
    # this is a dictionary with all the numbers
    numbers = {
        "1": "One",
        "2": "Two",
        "3": "Three",
        "4": "Four",
        "5": "Five",
        "6": "Six",
        "7": "Seven",
        "8": "Eight",
        "9": "Nine",
        "0": "Zero",
        " ": " "
    }

    output = ""
    # we define a for loop here
    for number in phone_number:
        output += numbers.get(number, "error") + " "
    print(output)
