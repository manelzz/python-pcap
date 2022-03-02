'''
DocString: Rock-Paper-Scissors
'''
 
import random
from tkinter import ROUND

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


end_game = False

while not end_game:
    
    end_round = False
    round_num = 0
    round_player_wins = 0
    round_player_drafts = 0
    round_player_losses = 0
 
    while not end_round:
        
        round_num += 1

        print(f"Let's start Game Round {round_num} (Best of 5 rounds)")
        print("1,2,3!!! Rock, paper and scissors")

        #get hand for player and computer
        while True:
            hand_player = input("Please, select a value (R:\U0001F44A | P:\U0000270B | S:\U0000270C) ") 
            if hand_player not in ("RSPrsp"):
                print("Error!! Enter a correct value")
            else: break
        hand_computer = random.choice("RSP")     
        
        #select the round results
        if hand_player == hand_computer:
            round_player_drafts += 1
            print(f"You select the same move!! {hand_player}")
        elif hand_player in "Rr" and hand_computer == "Ss":
            round_player_wins += 1
            print(f"You wins!! {hand_player} vs {hand_computer}")
        elif hand_player == "Ss" and hand_computer == "Pp":
            round_player_wins += 1
            print(f"You wins!! {hand_player} vs {hand_computer}")
        else:
            round_player_losses += 1
            print(f"You lost!! {hand_player} vs {hand_computer}")
  
        #Print round report
        print("Round report!")
        print("*" *50)
        print(f"Round Nº: {round_num}")
        print(f"Player: \
                Wins: {round_player_wins/round_num:.2%} \
                Lost: {round_player_losses/round_num:.2%} \
                Draft: {round_player_drafts/round_num:.2%}")
        print(f"Computer: \
                Wins: {round_player_losses/round_num:.2%} \
                Lost: {round_player_wins/round_num:.2%} \
                Draft: {round_player_drafts/round_num:.2%}")
        print("*" *50)

        #Check if a player wins more than games or the limit of round is achieved
        end_round = False if round_wins < (MAX_ROUNDS-round_wins) else True
        end_round = False if round_num < MAX_ROUNDS else True
        
  
    while True: 
        new_game = input(f"Do you want to play again? [Y]/[N]: ")
        if new_game not in ("ynYN"):
            print("Error!! Enter a correct value")
        else: break
    
    end_game = False if new_game in "yY" else True
    
    #Print Game report
    print(f"Selected: {end_game}")
    print("Game report!")
    print("*" *50)
    print("*" *50)

print("Thank you!! See you soon!!!!")

