'''
DocString: Rock-Paper-Scissors
'''
 
import random

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
        pass # sacar mano
        pass # mostrar estadisticas
    
    new_game = input(f"Do you want to play again? (y/n): ")
    if  new_game == "n":
        end_game = True
    elif new_game == "y":
        pass
    else: 
        print("")

print("Thank you!! See you soon!!!")

