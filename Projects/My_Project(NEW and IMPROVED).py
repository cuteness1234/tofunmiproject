import random

lower_bound = 1
upper_bound = 100

number = random.randint(lower_bound, upper_bound)

points = 1000


def check_guess(guess):
    global lower_bound, upper_bound, points
    if guess == number:
        return f"You got it! Your final score: {points} points", True
    points -= 50
    if guess < number:
        lower_bound = guess + 1
        return "Almost there, just a bit higher", False
    else:
        upper_bound = guess - 1
        return "Almost there, just a bit lower", False


while True:
    guess = input(f"Please type a number between {lower_bound} and {upper_bound}: ")
    guess = int(guess)

    message, finished = check_guess(guess)
    print(message)
    if finished:
        break