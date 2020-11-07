from random import randint

player_choice = input ("Enter Rock, Paper or Scissor: ")

possible_choices = ["Rock", "Paper", "Scissor"]

computer_choice = possible_choices[randint(0,2)]

print(player_choice)
print(computer_choice)