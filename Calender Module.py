import calendar

print(calendar.weekheader(3))
print()

print(calendar.firstweekday())
print()

print(calendar.leapdays(2010, 2021))
print()

print(calendar.month(2020, 3))
print()

print(calendar.calendar(2020))
print()

print(calendar.isleap(2020))

if calendar.isleap(2020):
    print('2020 is a leap year.')
else:
    print('NOE')