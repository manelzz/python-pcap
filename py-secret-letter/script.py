'''
Python DocString: The secret letter game
'''

import random
import string

def main():

    '''
    Main module Method
    '''
    
    print("*" * 150)
    print("S E C R E T  L E T T E R  G A M E")
    print("*" * 150)

    player_name = input("Hello! What's your name? ")
    print(f"Welcome, {player_name}! I'm thinking a letter between A and Z, Can you guess it? ")

    secret_letter = random.choice(string.ascii_uppercase)
    num_attempts = 0

    secret_found = False

    while not secret_found:
        num_attempts += 1

        print("-" * 100)
        player_letter = input(f"Attempt {num_attempts} > Please {player_name}, select a letter  between A-Z: " )
        print("-" * 100)

        #Capitalize the letter
        player_letter = player_letter.upper()

        if player_letter == secret_letter:
            print(f"Congratulations {player_name}! The secret letter was {secret_letter} and you guessed it at attempt {num_attempts}.")
            secret_found = True
        elif player_letter < secret_letter:
            print(f"Sorry {player_name}! Your guess is to low:")
        elif player_letter > secret_letter:
            print(f"Sorry {player_name}! Your guess is to high:")

    print(f"Good job! Thanks for playing with us")

#Call the main method
if __name__ == "__main__":
    main()
