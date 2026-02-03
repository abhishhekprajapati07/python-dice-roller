"""
Docstring for Exersice - Roll a dice
write a program to simulate a roll of a die/dice
A die has 6 faces of numbers 1 to 6 written on them
The program should randomly print a number between 1 to 6
"""

import random

print("Welcome to the game of rolling a dice.")

while True:
    choice = input("Press 'Enter' to roll a dice or 'q' to quit.")
    choice = choice.strip()
    if choice == 'q':
        print("Thanks for playing a game, bye!!")
        break
    elif choice == '':
        number = random.randint(1, 6)
        print(f"Your number is {number}")
    else:
        print("Invalid input!!")

print("GAME OVER!!!")
