# a quick game of rock-paper-scissors against a random num
from random import randint

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
def convert_choice(choice: int):
  if choice == 1:
    return "rock:" + rock + "\n"
  elif choice == 2:
    return "scissors:" + scissors + "\n"
  elif choice == 3:
    return "paper:" + paper + "\n"
  else:
    return "ERROR"

def decide_winner(player_choice: int, comp_choice: int):
  print(f"\nYou chose {convert_choice(player_choice)}\nI chose {convert_choice(comp_choice)}")
  if player_choice == comp_choice-1 or player_choice == comp_choice + 2:
    print("You won!\n\n")
  elif player_choice == comp_choice:
    print("We tied!\n\n")
  else:
    print("You lost.\n\n")
  
def app():
  flag = True
  options = """Make your choice!
1 -> rock
2 -> scissors
3 -> paper
0 -> quit
"""
  print("Let's play Rock Paper Scissors!")
  while flag:
    print(options)
    player_choice = int(input("> "))
    comp_choice = randint(1, 3)
  
    if player_choice == 0:
      flag = False
    elif player_choice > 0 and player_choice < 4:
      decide_winner(player_choice, comp_choice)
    else:
      print("I didn't recognize that option.")
  print("Exiting...\n\nThanks for playing!")

app()