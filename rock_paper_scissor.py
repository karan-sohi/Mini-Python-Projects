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

options = []
options.extend([rock, paper, scissors])
computer_choice = random.choice(options)
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors \n"))
if user_choice == 0:
    print(options[0])
elif user_choice == 1:
    print(options[1])
else:
    print(options[2])

print("Computer chose:")
print(computer_choice)

win_msg = "You Win!"
lose_msg = "You lose!"

if user_choice == 0 and computer_choice == options[2]:
    print(win_msg)
elif user_choice == 1 and computer_choice == options[0]:
    print(win_msg)
elif user_choice == 2 and computer_choice == options[1]:
    print(win_msg)
elif (user_choice == options.index(computer_choice)):
    print("Match Draw")
else:
    print(lose_msg)

