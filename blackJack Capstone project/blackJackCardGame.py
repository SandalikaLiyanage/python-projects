import random
import os
from art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#1
def deal_card():
    """Returns a random card from the deck"""
    select_card=random.choice(cards)
    return select_card

#(a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
def calculate_score(card_list):
    """Take a list of cards and calculate the sum of the cards"""
    if sum(card_list)==21 and len(card_list)==2:
        return 0
    if 11 in card_list and sum(card_list)>21:
        card_list.remove(11)
        card_list.append(1)
    
    total = sum(card_list)
    return total

def compare(user,computer):
    if user==computer:
        print("Draw 🙃")
    elif computer==0:
        print("Dealer has Blackjack!, You lose 😤")
    elif user==0:
        print("You has Blackjack!, You win 😁")
    elif user>21:
        print("You went over, You lose 😤")
    elif computer>21:
        print("Dealer went over, You win 😁")
    elif user>computer:
        print("You win 😁")
    else:
        print("You lose 😤")

def play_game():
    
    print(logo)

    user_cards = []
    computer_cards = []

    is_game_over=False
    for i in range(1,3):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card : {computer_cards[0]}")

        if user_score==0 or computer_score==0 or user_score>21:
            is_game_over=True
        else:
            x=input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if x=="y":
                user_cards.append(deal_card())
            else:
                is_game_over=True

    #dealer strategy
    while computer_score<17 and computer_score !=0:
        computer_cards.append(deal_card())
        computer_score=calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    compare(user_score,computer_score)

while (input("Do you want to play a game of Blackjack? Type 'y' or 'n': "))=="y":
    os.system('cls')
    play_game()