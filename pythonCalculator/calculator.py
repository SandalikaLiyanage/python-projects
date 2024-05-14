# calculator
# add
import os
from art import logo

def add(n1,n2):
    return n1+n2

# substract
def substract(n1,n2):
    return n1-n2

# multiply
def multiply(n1,n2):
    return n1*n2

# dicide
def divide(n1,n2):
    return n1/n2

operators={
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}
def calculator():
    print(logo)
    num1=float(input("What's the first number?: "))

    for operator in operators:
        print(operator)

    x="y"
    while x=="y":
        operation_symbol=input("Pick an operation: ")
        num2=float(input("What's the next number?: "))

        function=operators[operation_symbol]
        answer=function(num1,num2)
        print(f"{num1}{operation_symbol}{num2}= {answer}")
        num1=answer
        x=input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation.: ").lower()
    os.system('cls')
    calculator()

calculator()
