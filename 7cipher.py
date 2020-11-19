import art
import words
from os import system

logo = art.caesar_logo
alphabet = words.alphabet

print(logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def repeat(answer_in):
    if answer_in == "yes":
        system('clear')
        print(logo)
        direction2 = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text2 = input("Type your message:\n").lower()
        shift2 = int(input("Type the shift number:\n"))
        caesar(text2, shift2, direction2)

def caesar(input_text, shift_amount, direction):
    output_text = ""

    if shift_amount > 26:
        shift_amount %= 26

    if direction == "decode":
        shift_amount *= -1

    for letter in input_text:

        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            output_text += alphabet[new_position]
        else:
            output_text += letter

    print(f"The {direction}d text is '{output_text}'.\n")
    answer_out = input("Would you like to go again?\n")
    repeat(answer_out)

caesar(text, shift, direction)




#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a new function that calls itself if they type 'yes'. 
