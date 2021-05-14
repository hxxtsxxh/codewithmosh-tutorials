# import time module
import time
import datetime

# 24-hour format below
print(time.strftime("%H:%M:%S"))

# 12-hour format below
print(time.strftime("%I:%M:%S"))

# datetime module

e = datetime.datetime.now()

print(e.strftime("%Y-%m-%d %H:%M:%S"))

print(e.strftime("%d/%m/%Y"))

print(e.strftime("%I:%M:%S %p"))

print(e.strftime("%a, %b %d, %Y"))
