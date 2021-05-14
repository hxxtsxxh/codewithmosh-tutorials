# names = ['John', 'Heet', 'Mary', 'Pari']  # this is a list
# print(names[0])  # this prints out the first thing on the list

numbers = [1, 2, 3, 4, 5, 3, 8, 10, 2, 3]
maxNumber = numbers[0]

for number in numbers:
    if number > maxNumber:
        maxNumber = number
print(maxNumber)
