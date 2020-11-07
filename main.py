from random import randint

player_choice = input ("Enter Rock, Paper or Scissor: ")

possible_choices = ["Rock", "Paper", "Scissor"]

computer_choice = possible_choices[randint(0,2)]

print("Player Choice: ",player_choice)
print("Computer Choice: ",computer_choice)

if player_choice == computer_choice:
  print ("Result: Tie")
elif player_choice == "Rock": 
  if computer_choice == "Scissor":
    print ("Result: Win")
  else:
    print ("Result: Lose") 
elif player_choice == "Scissor":
  if computer_choice == "Paper":
    print ("Result: Win")
  else:
    print ("Result: Lose")  
elif player_choice == "Paper": 
  if computer_choice == "Scissor":
    print ("Result: Lose")
  else: 
    print ("Result: Win")  
else:
  print("Please try again, invalid choice!")
