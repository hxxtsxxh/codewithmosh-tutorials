# from modules import converters # modules is a directory
# from modules import mathops

# ! here we are using the 'converters' module that we created
# print(str(round(converters.kg_to_lbs(70))) + ' lbs')

# ! here we are using the 'mathops' module that we created
# print(mathops.sub(7,8))

# EXERCISE
from modules.utils import find_max

numbers = [0, 5, 6, 13, 4, 6, 8, 10]

result = find_max(numbers)

print(result)
