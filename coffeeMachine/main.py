MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit=0
#function to check if the ingredients are enough for the drink
def drink_ingredients_check(drink,profit):
        for i in MENU:
            if i==drink:
                if (resources["water"]>=MENU[i]["ingredients"]["water"]) :
                    if (resources["coffee"]>=MENU[i]["ingredients"]["coffee"]):                       
                        if resources["milk"] >= MENU[i]["ingredients"].get("milk", 0):
                            print("Please insert coins")  
                            sum=money_collect()
                            y=drink_cost_check(sum,drink)
                            if y==False:
                                return profit
                            else:
                                profit=profit+y
                                for k in resources:
                                    resources[k]=resources[k]-MENU[i]["ingredients"].get(k, 0)
                                return profit
                        else:
                            print("Sorry there is not enough milk")
                    else:
                        print("Sorry there is not enough coffee")
                else:
                    print("Sorry there is not enough water")
            else:
                continue

#function to check the amount
def drink_cost_check(total,drink):
    for i in MENU:
        if i==drink:
            if total>=MENU[i]["cost"]:
                balance=total-MENU[i]["cost"]
                print(f"Here is {balance:.2f} in change")
                print(f"Here is your ☕{i}. Enjoy!")
                return MENU[i]["cost"]
            else:
                print("Sorry that's not enough money. Money refunded.")
                return  False
        else:
            continue

def money_collect():
            total=0
            quater=float(input("How many quaters?:"))
            dime=float(input("How many dimes?:"))
            nickle=float(input("How many nickles?:"))
            penny=float(input("How many pennies?:"))
            #quarters=$0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
            total=quater*0.25+dime*0.10+nickle*0.05+penny *0.01
            return total


x=True       
while x: 
    drink=input("What would you like (espresso/latte/cappuccino): ").lower()
    if drink=="report":
        print (resources)
        print(f"Money: ${profit}")
    elif drink=="off":
        x=False 
    else:
        profit=drink_ingredients_check(drink,profit)
        

        
        


