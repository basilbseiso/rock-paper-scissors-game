import random


print("Rock, Paper, Scissors, Shoot!")

#prompt user for input

#x = input("Choose 'rock" or 'paper' or 'scissors'")

user_choice = input("Choose 'rock' or 'paper' or 'scissors': ")
print("User chose:")
print(user_choice)

# Computer choice (at random)

options = ["rock", "paper", "scissors"]

computer_choice = random.choice(options)
print("Computer chose:")
print(computer_choice)