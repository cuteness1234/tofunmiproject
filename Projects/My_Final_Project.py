import random
import tkinter as tk

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
        return f"Please type a number between {lower_bound} and {upper_bound}. Your current point is {points}: ", False
    elif guess > 100:
        return "You entered a number greater than 100. Try again: ", False
    else:
        upper_bound = guess - 1
        return f"Please type a number between {lower_bound} and {upper_bound}. Your current point is {points}: ", False

def read_number(e=None):
    guess = el.get()
    try:
        guess = int(guess)
        message, finished = check_guess(guess)
        label_str.set(message)
        if finished:
            el.config(state=tk.DISABLED)
    except ValueError:
        label_str.set("Please enter a valid integer.")

def clear_screen():
    el.delete(0, tk.END)
    label_str.set(f"Type a number between {lower_bound} and {upper_bound}. Your remaining point is: {points}")

master = tk.Tk()
master.geometry("600x300")
master.title("Number Guessing Game :)")

label_str = tk.StringVar()
tk.Label(master, textvariable=label_str).grid(row=0)
label_str.set(f"Type a number between 1 and 100. You have {points}. You lose 50 points each time you guess wrong :)")

el = tk.Entry(master)
el.grid(row=1, column=0)

el.bind("<Return>", read_number)
tk.Button(master, text='Send', command=read_number).grid(row=2, column=0, sticky=tk.W, pady=4, padx=10)
tk.Button(master, text='Clear', command=clear_screen).grid(row=3, column=0, sticky=tk.W, pady=4, padx=10)


master.configure(background='cyan')
master.mainloop()
