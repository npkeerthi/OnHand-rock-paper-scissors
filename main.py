import random

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

user_choice = int(input("What is your choice? 0 for 'Rock', 1 for 'Paper' and 2 for 'Scissors'\n"))
if user_choice >= 0 and user_choice <= 2:
  images = [rock, paper, scissors]

  computer_choice = random.randint(0,2)

  map = [
  ["draw", "lose", "win"],
  ["win","draw", "lose"],
  ["lose", "win", "draw"]]
#1=rock
#1's rock draw, paper lose , sci win
#2=pape
#2's rock win , paper draw, sci lose
#3= scissors
#3's rock los, pap win , sc draw
  result = map[user_choice][computer_choice]

  print(f"Your choice was:\n{images[user_choice]}")
  print(f"The computer chose:\n{images[computer_choice]}")
  print(f"You {result}")
else:
  print("Invalid input")
