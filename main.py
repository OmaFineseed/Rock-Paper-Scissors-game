from ast import Continue
import random
from tkinter.messagebox import YES
import math

print("*****WELCOME TO RPS GAME*****\n RPS means ROCK, PAPER, SCISSORS \n Carefully, read the RULES of the game before you begin!")
print("This game is between you and the computer /CPU.")
print("****These are the RULES of the game***** :\n You will have to choose either R, S, or P to play")
print("Rock beats Scissors\n Paper beats Rock\n Scissors beats Paper")
print("If You and computer choose the same options, it is a TIE\n If You choose R and computer choose S OR\n You choose P and computer choose R OR\n You choose S and computer choose P. You WIN! and the computer LOOSE")
print("If You choose S and computer choose R OR\n You choose R and computer choose P OR\n You choose P and computer choose S. You LOOSE and the computer WINS!")
print("   ")

while True:
    options = ['R', 'P', 'S']
    cpu_option = random.choice(options)
    player_option = None
    
    while player_option not in options:
        player_option = input("Make a choice R for Rock, P for Paper or S for Scissors: ").upper()
        
        if player_option == cpu_option:
            print("Player:" ,player_option)
            print("Computer:",cpu_option)
            print("it's a TIE")
        elif player_option == "R":
            if cpu_option == "S":
             print("Player:" ,player_option)
             print("Computer:",cpu_option) 
             print("YOU WIN! ; Computer LOOSE")
             
            if cpu_option == "P":
             print("Player:" ,player_option)
             print("Computer:",cpu_option)
             print("YOU LOOSE ; Computer WINS!")
             
        elif player_option == "p":
            if cpu_option == "S":
             print("Player:" ,player_option)
             print("Computer:",cpu_option) 
             print("YOU LOOSE ; Computer WINS!")
                 
            if cpu_option == "R":
             print("Player:" ,player_option)
             print("Computer:",cpu_option)
             print("YOU LOOSE ; Computer WINS!")
               
               
        elif player_option == "S":
            if cpu_option == "P":
             print("Player:" ,player_option)
             print("Computer:",cpu_option)
             print("YOU WIN! ; Computer LOOSE")
             
            if cpu_option == "R":
             print("Player:" ,player_option)
             print("Computer:",cpu_option)
             print("You WIN! ; Computer LOOSE")
             
    Continue = input("keep playing? YES or NO: ").upper()
    if Continue == "YES":
        pass
    elif Continue == "NO":
        break
    else:
        break
print ("*****GOODBYE*****")         
