from game_data import data
from random import randint
from art import logo
from art import vs
import os
#select random 2 people from the list
length=len(data)-1
def choose_item():
    """choose a random item from game data"""
    item=randint(0,length)
    name=data[item]["name"]
    description=data[item]["description"]
    country=data[item]["country"]
    print(f"{name}, {description},from {country}")
    return item

def check_answer(answer):
    if answer=="A":
        if data[a]["follower_count"]>data[b]["follower_count"]:
            
            print("You're right!" ,end="")
            return True
        else:
            print(f"You are wrong ",end="")
            return False
    elif answer=="B":
        if data[b]["follower_count"]>data[a]["follower_count"]:
            
            print(f"You're right!" ,end="")
            return True
        else:
            print(f"You are wrong ",end="")
            return False

print(logo)
print(f"Compare A: " ,end="")
a=choose_item()

score=0
x=True   
while x:
    
    print(vs)
    print(f"Against B: " ,end="")
    b=choose_item()

    #fuction to check which item is higher 

    answer=input("Who has more followers? Type 'A' or 'B':").upper()
    os.system('cls')
    print(logo)
    x=check_answer(answer)
    if x==True:
        score+=1
        print(f"current score:{score}")
        a=b
        print(f"Compare A: " ,end="")
        print(f"{data[b]["name"]}, {data[b]["description"]}, from {data[b]["country"]}")
print(f"final score:{score}")


