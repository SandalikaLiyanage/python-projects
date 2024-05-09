from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

def caesar(text, shift, direction):
    
    length = len(alphabet)
    end_text = ""
    
    shift %= length
    if direction == "decode":
            shift *= -1
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift
            if(new_position>=length):
                new_position%=length
            new_letter = alphabet[new_position]
            end_text += new_letter
        else:
            end_text+=letter
    print(f"The {direction}d text is {end_text}")
x="yes"
while x=="yes": 
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)
    x=input("Type 'yes' if you want to go again, otherwise type 'no' :" ).lower()
print("Good bye")

    