import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))  # Replace with your desired dimensions

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up game window
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Number Guessing Game")

# Generate a random number within the specified range
lower_bound = 1
upper_bound = 100
number = random.randint(lower_bound, upper_bound)

# Initialize game variables
points = 1000
font = pygame.font.Font(None, 36)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get user input
    guess_text = input(f"Please type a number between {lower_bound} and {upper_bound}: ")
    try:
        guess = int(guess_text)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        continue

    # Check if the guess is correct
    if guess == number:
        print(f"You got it! Your final score: {points} points")
        pygame.quit()
        sys.exit()
    elif guess < number:
        print("Almost there, just a bit higher")
        lower_bound = guess + 1
    else:
        print("Almost there, just a bit lower")
        upper_bound = guess - 1

    # Update points
    points -= 50

    # Display points on the screen
    screen.fill((255, 255, 255))
    text_surface = font.render(f"Points: {points}", True, (0, 0, 0))
    screen.blit(text_surface, (10, 10))
    pygame.display.flip()

