'''
Python DocString: The secret number game
'''

import datetime
import random
import time

from numpy import number
from psutil import MACOS
from sqlalchemy import false, true

print("*" * 150)
print("S E C R E T  N U M B E R  G A M E")
print("*" * 150)

player_name = input("Hello! What's your name? ")
MAX_VALUE = int(input("Please, select the maximum number: "))
print(f"Welcome, {player_name}! I'm thinking a number between 1 and {MAX_VALUE}, Can you guess it?")

secret_number = random.randint(a=1, b=MAX_VALUE)
num_attempts = 0

secret_found = False

while not secret_found:
    num_attempts += 1

    print("-" * 100)
    player_number = int(input(f"Attempt {num_attempts} > Please {player_name}, select a number between 1 and {MAX_VALUE}: "))
    print("-" * 100)

    if player_number == secret_number:
        print(f"Congratulations {player_name}! The secret number was {secret_number} and you guessed it at attempt {num_attempts}.")
        secret_found = True
    elif player_number < secret_number:
        print(f"Sorry {player_name}! Your guess is to low:")
    elif player_number > secret_number:
        print(f"Sorry {player_name}! Your guess is to high:")

print(f"Good job {player_name}! Thanks for playing with us")
