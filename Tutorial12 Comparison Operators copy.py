name = input("What is your name? ")
char_count = len(name)

if char_count < 3:
    print("Name must be at least 3 characters long.")
elif char_count > 50:
    print("Name can only be a maximum of 50 characters")
else:
    print("Name Verified!")
