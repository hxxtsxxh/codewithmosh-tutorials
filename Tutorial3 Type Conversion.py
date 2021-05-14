weightLbs = input('Enter your current weight in lbs: ')
# We put int in front of our lbs var to convert str to int. Then we print the float value of kg weight.
weightKg = int(weightLbs) / 2.205
print(float(round(weightKg)))
