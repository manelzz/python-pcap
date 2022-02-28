'''
DocString: Rock-Paper-Scissors
'''
 
import random

from numpy import round_

# Variables
player_name = None
MAX_ROUNDS = 5
total_games = 0
total_wins = 0
total_losses = 0
round_num = 0
round_wins = 0
round_drafts = 0
round_losses = 0
computer_move = None
player_move = None 

# Main
print ("*" * 150)
print (" Welcome to Rock Paper Scissor Game (\U0001F44A \U0000270B \U0000270C)")
print ("*" * 150)

player_name = input("Hello, What's your name? --> ")
print(f"\nWelcome, {player_name}! We will play the famous game rock, paper and scissors.")
print("The winner will be the best of 5 rounds. Are you ready?")
print("-" * 150)

#while 
print("Let's start Game Round {round_num} (Best of 5 rounds)")

print("1,2,3!!! Rock, paper and scissors")
input("Please, select a value (R:\U0001F44A | P:\U0000270B | S:\U0000270C) ") 

end_game = False
end_round = False

while not end_game:
    
    round_num = 0
    round_wins = 0
    round_drafts = 0
    round_losses = 0
 
    while not end_round:
        
        round_num = +1
        
        pass # sacar mano
        
        pass # mostrar estadisticas
    
        #Print round report
        print("Round report!")
        print("*" *50)
        print(f"Wins: {round_wins/round_num:.2%}")
        print("*" *50)

        #Check if a player wins more than games or the limit of round is achieved
        end_round = False if round_wins < (MAX_ROUNDS-round_wins) True
        end_round = False if round_num < MAX_ROUNDS True
        

    new_game = input(f"Do you want to play again? (y/n): ")
    if  new_game == "n":
        end_game = True
    elif new_game == "y":
        pass


    #Print Game report
    print("Game report!")
    print("*" *50)
    print("*" *50)

print("Thank you!! See you soon!!!!")

