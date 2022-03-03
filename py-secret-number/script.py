'''
Python DocString: The secret number game
'''

import random
import datetime as dt
import time

def main():
    '''
    Main Module Method
    '''
    print("*" * 150)
    print("S E C R E T  N U M B E R  G A M E")
    print("*" * 150)

    start_date = dt.datetime.now()
    player_name = input("Hello! What's your name? ")
    MAX_VALUE = int(input("Please, select the maximum number: "))
    print(f"Welcome, {player_name}! I'm thinking a number between 1 and {MAX_VALUE}, Can you guess it?")

    print(f"Loading game. Please wait ... {len(player_name)} seconds...")
    for t in range(1,len(player_name)):
        print(f"Waiting to start ... Seconds: {t} ")
        time.sleep(1)

    start_date = dt.datetime.today()
    print(F"start date: {start_date}")
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
    
    end_date = dt.datetime.today()
    duration = end_date - start_date

    print(f"Total duration: {duration.total_seconds():.2f} seconds")
    print(f"Good job {player_name}! Thanks for playing with us")

#Call the main method
if __name__ == "__main__":
    main()