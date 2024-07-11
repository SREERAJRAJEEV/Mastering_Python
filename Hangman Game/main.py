"""
main.py

This script implements the classic Hangman game. Hangman is a word-guessing game where players try to guess a word by suggesting letters. The game ends when the player successfully guesses the word or exhausts a predefined number of incorrect guesses, resulting in the completion of a hangman figure.

Modules:
    random: Used for selecting a random word from the word list.
    words: Contains the list of possible words for the game.
    logo: Contains the game logo and the stages of the hangman figure.

Functions:
    None

Execution:
    The script runs an interactive loop that allows the user to play multiple rounds of Hangman. After each round, the user is prompted to decide whether to continue or exit the game.

Gameplay:
    1. The game selects a random word from the word list.
    2. The word is displayed as a series of underscores, each representing a letter in the word.
    3. The player guesses letters one at a time.
    4. If the guessed letter is in the word, the corresponding underscores are replaced with the letter.
    5. If the guessed letter is not in the word, the game progresses the hangman figure.
    6. The player wins if they guess all the letters in the word before the hangman figure is complete.
    7. The player loses if the hangman figure is completed before the word is fully guessed.
    8. After each round, the player is asked if they want to play another round or exit the game.

Example:
    To run the game, execute the following command in the terminal:
        python main.py

Note:
    Ensure that `words.py` and `logo.py` are in the same directory as `main.py`.

"""
import random
from words import wordlist
from logo import logo,stages


#Select a random word
game = True
print(logo)
while game:
    select = random.randint(0, len(wordlist) - 1)
    word = wordlist[select].lower()
    print(word)

    #Display "_" as many as needed
    display = []
    for i in word:
        display += "_"

    print(display)

    flag = False
    incorrect = 0

    while (incorrect > -7):

        #Take users guess as input
        guess = input("Enter your guess: ")
        guess = guess.lower()

        #If guess is right, replace the "_" with the alphabet
        for i in range(0, len(word)):
            if guess == word[i]:
                display[i] = guess
        if guess not in word:
            incorrect -= 1
            print(stages[incorrect])
        print(display)

        if word == "".join(display):
            print("\nYou won!!\n")
            break

    if (incorrect == -7):
        print("\nOops you lost!!\n")

    print("\n***** Game over!! *****\n")
    print("\n****************************************************\n")

    game_continue = input("Do you wish to continue? (y/n) : ")

    if game_continue.lower() == 'n':
        game = False

