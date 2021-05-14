course = 'Python for beginners'
# to calculate the number of characters in this string, we use a method called "len."
print(len(course))
# now if we want to make our text in course all lowercase or uppercase, we use the dot operator.
print(course.lower())
# you can also do all uppercase
print(course.upper())
# Reminder: these changes wont change our original string.
print(course)

# lets say we want to know at what position is a certain letter. To do this, do the following command.
print(course.find('P'))
# this gives us an output of 0 as it is the "0th" position in the sentence.

# if we want to replace a certain part of a string, then we pass the course.replace command as shown
print(course.replace('beginners', 'Absolute Beginners'))
# even this will not change our original string
print(course)
print('Python' in course) # this will output whether the word, Python is in our text.
