from random import randint
EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5
turns=0

def check_answer(guess, answer,turns):
    """checks answer and return the no of turns remaining"""
    if guess>answer:
        print("Too high")
        return turns-1
    elif guess<answer:
        print("Too low")
        return turns-1
    else:
        print(f"right! {answer}")

def set_difficulty():
    level=input("Choose a difficulty")
    if level=="easy":
        return EASY_LEVEL_TURNS
    elif level=="hard":
        return HARD_LEVEL_TURNS
    
def game():
    #chosing a random number 1 an 100
    answer=randint(1,101)


    #set difficulty function

    turns=set_difficulty
    

   
    #repeat the gussing functionalty if they get it wrong
    guess=0
    while guess!=answer:
        print(f"You have {turns} ")
    #let the user guess a number
        guess=int(input("Make a guess"))

        #function to check users guess
        turns=check_answer(guess, answer,turns)

        # track the number of turns and reduce by 1 if they got wrong
        if turns==0:
            print("You run out of loses")
            return
        elif guess!=answer:
            print("Guess again")
    game()



