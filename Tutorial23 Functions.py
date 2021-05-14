def greet_user():
    greetings = 'Hi There!'
    print(greetings)
    print('Welcome Aboard!')
    print(len(greetings))
    foods = {
        "apple": '1',
        "orange": '2',
        "grape": '3'
    }
    print(foods.get('1'))


print("Start")
greet_user()
print("Finish")
