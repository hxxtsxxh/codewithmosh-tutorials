# two lists -numbers, uniques
# the "numbers" list contains numbers that are repetetive.
# the "uniques" list is blank so only one of the repetetive numbers can be appended into the list.
numbers = [1, 2, 3, 4, 5, 6, 9, 1, 4, 2, 5, 10, 4, 7, 6, 10]
uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number) 
print(uniques)
