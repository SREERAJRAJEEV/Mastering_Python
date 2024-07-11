"""
Caesar Cipher Encryption and Decryption

This script provides functions to encrypt and decrypt messages using the Caesar Cipher technique.
It includes a command-line interface for user interaction.

Usage:
- Run the script and follow the prompts to 'encode' or 'decode' a message.
- Specify the message and the shift number to perform the operation.

For more details, refer to the README.md file.

"""

from logo import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

##Define function to encrypt the message
def encrypt(text, shift):
    l = len(alphabet)
    code = ""
    for char in text:
        if char in alphabet:
            index = alphabet.index(char)
            new_index = (index+shift)%l
            code = code + alphabet[new_index]
    print(code)

#Define function to decrypt the message
def decrypt(text, shift):
    l = len(alphabet)
    code = ""
    for char in text:
        if char in alphabet:
            index = alphabet.index(char)
            new_index = (index-shift)%l
            code = code + alphabet[new_index]
    print(code)


print(logo)

while(True):

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")


    if direction == "encode" or direction == "decode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        #Perform operation corresponding to the user's choice
        if direction == "encode":
            encrypt(text, shift)
        elif direction == "decode":
            decrypt(text,shift)
        else:
            print("Invalid input")

    else:
        print("Invalid input")
        break

