#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# for l in range(1,nr_letters+1):
#     x=random.randint(0,len(letters)-1)
#     print(letters[x], end="")
# for l in range(1,nr_numbers+1):
#     x=random.randint(0,len(numbers)-1)
#     print(numbers[x], end="")
# for l in range(1,nr_symbols+1):
#     x=random.randint(0,len(symbols)-1)
#     print(symbols[x], end="")



#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
array=[]
for l in range(1,nr_letters+1):
    x=random.randint(0,len(letters)-1)
    array.append(letters[x])
for l in range(1,nr_numbers+1):
    x=random.randint(0,len(numbers)-1)
    array.append(numbers[x])
for l in range(1,nr_symbols+1):
    x=random.randint(0,len(symbols)-1)
    array.append(symbols[x])
length=len(array)

random.shuffle(array)

for j in range(0,length):
    print(array[j], end="")

