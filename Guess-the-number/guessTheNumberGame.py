import random
from art import logo
answer=random.randint(1,101)
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
#print(f"Pssst, the correct answer is {answer}")
level=input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if level=="hard":
    attempts=5
else:
    attempts=10
for i in range(attempts,0,-1):
    print(f"You have {i} attempts remaining to guess the number.")
    guess=int(input("Make a guess: "))
    if guess<answer:
        print("Too low.")
        if i!=1:
            print("Guess again")
    elif guess>answer:
        print("Too high.")
        if i!=1:
            print("Guess again")
    else:
        break
if(answer==guess):
    print(f"You got it! The answer was {answer}")
else:
    print("You've run out of guesses, you lose.")

