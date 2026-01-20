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

import random

list = [rock,paper,scissors]

user_choice = input("What do you choose? Rock, paper or scissors?").lower()
if user_choice == "rock":
    user_choice=0
elif user_choice == "paper":
    user_choice = 1
elif user_choice == "scissors":
    user_choice = 2
else:
    print("Please select one of the given options.")

print(list[user_choice])

system_choice = random.randint(0,2)
print("The computer chose:\n"+list[system_choice])

if user_choice == 0:
    if system_choice == 2:
        print("YOU WIN!!! :)")
    elif system_choice == 1:
        print("You lose. :(")
    else:
        print("It is a draw. :|")
elif user_choice == 1:
    if system_choice == 0:
        print("YOU WIN!!! :)")
    elif system_choice == 2:
        print("You lose. :(")
    else:
        print("It is a draw. :|")
elif user_choice == 2:
    if system_choice == 1:
        print("YOU WIN!!! :)")
    elif system_choice == 0:
        print("You lose. :(")
    else:
        print("It is a draw. :|")