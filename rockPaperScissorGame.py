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

# Write your code below this line 👇
import random

user_pick = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))



if user_pick == 0:
    user_pick = rock
elif user_pick == 1:
    user_pick = paper
else:
    user_pick = scissors
print(user_pick+"\n")
com_pick = random.randint(0, 2)

if com_pick == 0:
    com_pick = rock
elif com_pick == 1:
    com_pick = paper
else:
    com_pick = scissors
print("Computer chose:\n")
print(com_pick + "\n")

if user_pick == rock and com_pick == scissors:
    print("You win")
elif user_pick == rock and com_pick == paper:
    print("You lose")
elif user_pick == rock and com_pick == rock:
    print("Draw")
elif user_pick == paper and com_pick == rock:
    print("You win")
elif user_pick == paper and com_pick == scissors:
    print("You lose")
elif user_pick == paper and com_pick == paper:
    print("Draw")
elif user_pick == scissors and com_pick == rock:
    print("You lose")
elif user_pick == scissors and com_pick == paper:
    print("You win")
else:
    print("Draw")
