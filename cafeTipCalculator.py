print("Welcome to the tip calculator!\n")
total=float(input("What was the total bill? $"))
tip=int(input("\nHow much tip would you like to give?10, 12 or 15? "))
tip_amount=total*(tip/100)
x=int(input("\nHow many people to split the bill? "))
payment=round((tip_amount+total)/x,2)
print(f"Each person should pay{payment}")


