"""
Name:           Robin Groot
Version:        1.0
Inputs:         Number start, number end,
Outputs:
Description:    Random number guesser
"""
import random

# Sets the amount of guesses allowed.
allowed_guess = int(input("How many times do you want to guess you can choose up to 5 times: "))
if not 1 <= allowed_guess <= 5:
    print("\nYou filled in a wrong amount try again.")
    allowed_guess = int(input("How many times do you want to guess you can choose up to 5 times: "))

# Making variables
guessed_right = False
amount_guess = 0
guess_list = []
guess_list_text = []
list_input = []

# Fills in the numbers you can choose between.
number_start = int(input("Choose number start: "))
number_end = int(input("Choose number end: "))
random_number = random.randint(number_start, number_end)

# The main function where it checks if you guessed right or
while not(guessed_right is True or amount_guess >= allowed_guess):
    guess = int(input(f"Choose a number from {number_start} till {number_end}: "))
    if random_number == guess:
        guessed_right = True
    else:
        # Looks if it is higher or lower to give you the right message ands adds 1 to the guess counter.
        guess_list.append(guess)
        if guess < random_number:
            amount_guess += 1
            if amount_guess >= allowed_guess:
                print("\nYou guessed wrong guess higher.")
        else:
            amount_guess += 1
            if amount_guess >= allowed_guess:
                print("\nYou guessed wrong guess lower.")

for x in guess_list:
    if x < random_number:
        guess_list_text.append(" Wrong, too low")
    else:
        guess_list_text.append(" Wrong, Too high")
    list_input = [z for z in zip(str(x), guess_list_text)]

# Gives you your result.
if guessed_right:
    print(f"\nYou guessed it right!!!"
          f"\nHere is your input: {list_input}")
else:
    print(f"\nYou used all your guesses."
          f"\nThe number was {random_number} here is your input: {list_input}")

