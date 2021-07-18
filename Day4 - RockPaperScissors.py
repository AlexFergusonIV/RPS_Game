# Day 4: Rock Paper Scissors
import math         #for math integers
import random       #for randomly generating computer input
import os
os.system('cls||clear') # this line clears the screen 'cls' = windows 'clear' = unix


dictionary  =   {0: "Rock", 1: "Paper", 2: "Scissors"}                        #Dictionary to assign integer keys to value of rock/paper/scissors


my_score    =   0
comp_score  =   0

print("Welcome to Alex's game of Rock Paper Scissors!  ")
play_rps = "y"
while (play_rps == "y"):
    
    choose  =   math.floor(int(input("\nWhat do you choose?  Type 0 for Rock, 1 for Paper, or 2 for Scissors:     ")))
    print("\n",choose,"\n")
    while choose not in [0, 1, 2]:
        choose    =   math.floor(int(input("That is an invalid input.  You need to input a 0, 1, or 2   :  ")))

    computer    =   random.randint(0,2)                                        #Randomly assign comp with 0, 1, or 2

## GAME LOGIC
    if choose == 0:                                                            #You chose rock
        if computer == 0:                                                           #Comp chose rock
            print("You both chose ", dictionary[computer], ".   IT'S A TIE!")

        elif computer == 1:                                                         #Comp chose paper
            print("You chose ", dictionary[choose], "and the computer chose ", dictionary[computer], ".     YOU LOSE!")
            comp_score += 1

        elif computer == 2:                                                         #Comp chose scissors
            print("You chose ", dictionary[choose], "and the computer chose ", dictionary[computer], ".     YOU WIN!")
            my_score += 1

    if choose == 1:                                                             #You chose paper
        if computer == 0:                                                           #Comp chose rock   
            print("You chose ", dictionary[choose], "and the computer chose ", dictionary[computer], ".     YOU WIN!")
            my_score += 1

        elif computer == 1:                                                         #Comp chose paper
            print("You both chose ", dictionary[computer], ".   IT'S A TIE!")

        elif computer == 2:                                                         #Comp chose scissors
            print("You chose ", dictionary[choose], "and the computer chose ", dictionary[computer], ".     YOU LOSE!")
            comp_score += 1

    if choose == 2:                                                             #You chose scissors
        if computer == 0:                                                           #Comp chose rock
            print("You chose ", dictionary[choose], "and the computer chose ", dictionary[computer], ".     YOU LOSE!")
            comp_score += 1

        elif computer == 1:                                                         #Comp chose paper
            print("You chose ", dictionary[choose], "and the computer chose ", dictionary[computer], ".     YOU WIN!")
            my_score += 1

        elif computer == 2:                                                         #Comp chose scissors
            print("You both chose ", dictionary[computer], ".   IT'S A TIE!")

## ASK TO REPLAY
    print("\nThe current score is: \nYOU: ", my_score, "   COMPUTER: ", comp_score)
    play_rps    =   input("\nWould you like to play again? Y/N   ").lower()
    
    while play_rps not in ["y", "n"]:
        play_rps    =   input("That is an invalid input.  You need to input Y/N:  ").lower()

## BREAK AFTER USER DOES NOT CHOOSE TO PLAY AGAIN
print("\nThe final score is:\nYOU: ", my_score, "   COMPUTER: ", comp_score, "\n \nThat ends our game.  Feel free to play again sometime!")