
from distutils.command.install_scripts import install_scripts
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
game_images=[rock,paper,scissors]
choosing_number =int(input('Choose "Bua" or "Giay" or "Keo" '))
print(game_images[choosing_number-1])
#raise computer 
computer_num =random.randint(1,3)
print(game_images[computer_num-1])

if (choosing_number==1 and computer_num==3) or(choosing_number==2 and computer_num==1) or(choosing_number==3 and computer_num==2):
    print("Win")
if (choosing_number==1 and computer_num==1) or(choosing_number==2 and computer_num==2) or(choosing_number==3 and computer_num==3):
    print("Tie")
if (choosing_number==1 and computer_num==2) or(choosing_number==2 and computer_num==3) or(choosing_number==3 and computer_num==1):
    print("Lose")