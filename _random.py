import random
number=random.randint(10,100)
while True:
    a=int(input('enter a number'))
    if number==a:
        print('congrats you guessed correct number')
    elif a < number:
        print('enter some greater number')
    else:
        print('enter some lesser number')


