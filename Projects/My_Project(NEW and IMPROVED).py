import random

lower_bound = 1
upper_bound = 100

number = random.randint(lower_bound, upper_bound)

points = 1000

while True:
    guess = input(f"Please type a number between {lower_bound} and {upper_bound}: ")
    guess = int(guess)

    if guess == number:
        print(f"You got it! Your final score: {points} points")
        break
    elif guess < number:
        print("Almost there, just a bit higher")
        lower_bound = guess + 1
    else:
        print("Almost there, just a bit lower")
        upper_bound = guess - 1

    points -= 50