import os
from art import logo
print(logo)
print("Welcome to the secret auction program")

auction={}
rerun="yes"
def add_to_auction(name,bid):
    auction[name]=bid
while rerun=="yes":
    name=input("What is your name? \n")
    bid=int(input("What is your bid: $")) 
    rerun=input("Are there any bidders? Type Yes or No: ").lower()
    add_to_auction(name,bid)
    os.system('cls')
os.system('cls')
max=0
for key in auction:
    if auction[key]>max:
        max=auction[key]
        winner=key
print(f"The winner is {winner} with a bid of ${max}.")   
    
