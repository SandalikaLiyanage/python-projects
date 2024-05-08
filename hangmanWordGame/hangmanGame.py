import random
import hangmanArt
import hangmanWord


print(hangmanArt.logo)
chosen_word = random.choice(hangmanWord.word_list)
stages=hangmanArt.stages
#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

display=[]
length=len(chosen_word)
for i in range(0,length) :
    display.append("_")
print(display)

# Use a while loop to let the user guess again.
# The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). 
#Then you can tell the user they've won.

lives =6

    
while not lives==0:
    if "_" in display:
        guess = input("Guess a letter: ").lower()

    #TODO-3: - Loop through each position in the chosen_word;
    #If the letter at that position matches 'guess' then reveal that letter in the display at that position.
    #e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
        if guess not in display:
            for position in range(0,length):
                if (chosen_word[position] == guess):
                    display[position]=guess 

            if guess in chosen_word:
                print("Letter is in the word")        
                print(display)
                print(stages[lives])
            else:
                print("Oops incorrect letter")
                print(display)
                print(stages[lives-1])
                lives-=1 
                if lives==0:
                    print("\n OH!! You lost!")
        else:
            print("You already entered that letter before")
    else:
        lives=0
        print(display)
        print("You won! YAY") 
            
    




