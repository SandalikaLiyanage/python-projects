print("Welcome to the treasure island!!\n")
turn=input("Where do you wanna turen(left/right)? ")
turn=turn.lower()
if(turn=='left'):
    river=input("/n Do you ant to swim the river or wait for a boat(wait/swim)? ")
    river=river.lower()
    if(river=='wait'):
        color=input("/n Which door will you choose(red /yellow/blue)?" ) 
        color=color.lower()
        if(color=="yellow"):
            print("you win!!")
        else:
            print("GAME OVER")
    else:
        print("GAME OVER")
else:
    print("GAME OVER")