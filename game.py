import os
from dotenv import load_dotenv

load_dotenv()

x = os.getenv("PLAYER_NAME")
print("------------------------")
print("Welcome", x ,"to my Rock-Paper-Scissors game...")

import random


print("Rock, Paper, Scissors, Shoot!")

#prompt user for input

#x = input("Choose 'rock" or 'paper' or 'scissors'")
print("------------------------")
user_choice = input("Choose 'rock' or 'paper' or 'scissors': ")
print("User chose:")
print(user_choice)

#adapted from Serena Barish example

if user_choice in ["rock","paper","scissors"]:
    print("And...")
else:
    print("Uh oh! Please try again and enter your choice in the correct format")
    exit()
# Computer choice (at random)

options = ["rock", "paper", "scissors"]

computer_choice = random.choice(options)
print("Computer chose:")
print(computer_choice)

print("------------------------")
if(user_choice == "rock" and computer_choice == "scissors"):
    print("Congratulations,you win!")
elif(user_choice == "rock" and computer_choice == "paper"):
    print("Oh, the computer won. It's ok.")
elif(user_choice == "paper" and computer_choice == "scissors"):
    print("Oh, the computer won. It's ok.")
elif(user_choice == "paper" and computer_choice == "rock"):
    print("Congratulations,you win!")
elif(user_choice == "scissors" and computer_choice == "rock"):
    print("Oh, the computer won. It's ok.")
elif(user_choice == "scissors" and computer_choice == "paper"):
    print("Congratulations,you win!")
else: print("It's a tie!")

print("------------------------")

print("Thanks for playing. Please play again!")