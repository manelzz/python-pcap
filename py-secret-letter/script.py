'''
Python DocString: The secret letter game
'''

from ast import While
import datetime
import random
import time
import string

from numpy import number
from sqlalchemy import false

print("*" * 150)
print("S E C R E T  L E T T B E R  G A M E")
print("*" * 150)

player_name = input("Hello! What's your name? ")
player_letter = input(f"Welcome, {player_name}! I'm thinking a letter between A and Z, Can you guess it?")

secret_letter = random.choice(string.ascii_uppercase)
num_attempts = 0

secret_found = False

while not secret_found:
    num_attempts += 1

    print("-" * 100)
    player_number = input(f"Attempt {num_attempts} > Please {player_name}, select a letter  between A-Z")
    print("-" * 100)

    if player_number == secret_letter:
        print(f"Congratulations {player_name}! The secret letter  was {secret_letter} and you guessed it at attempt {num_attempts}.")
        secret_found = True
    elif player_number < secret_letter:
        print(f"Sorry {player_name}! Your guess is to low:")
    elif player_number > secret_letter:
        print(f"Sorry {player_name}! Your guess is to high:")

print(f"Good job {player_name}! Thanks for playing with us")