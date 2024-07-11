"""
logo.py

This module contains the visual elements used in the Hangman game, including the game logo and the stages of the hangman figure. These elements are used to enhance the user experience by providing visual feedback during the game.

Modules:
    None

Attributes:
    logo (str): The ASCII art logo for the Hangman game, displayed at the start of the game.
    stages (list): A list of strings, each representing a stage of the hangman figure. The stages depict the progress of the hangman as incorrect guesses are made.

Usage:
    This module is imported by `main.py` to display the game logo at the start and to show the progress of the hangman figure based on the number of incorrect guesses.

Example:
    Importing the logo and stages in another script:
        from logo import logo, stages

Note:
    You can modify the `logo` and `stages` to customize the visual elements of the game.
"""

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
