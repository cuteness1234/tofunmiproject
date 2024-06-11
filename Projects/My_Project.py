print('Let us start')
import random

number = random.randint(1, 100)

guess = None
count = 1

while True:
    guess = input('Please type a number between 1 and 100: ')
    guess = int(guess)

    if guess == number:
        print('You got it')
        break
    elif guess < number:
        print('Almost there just a bit higher')
    else:
        print('Almost there just a bit lower')


    count += 1
