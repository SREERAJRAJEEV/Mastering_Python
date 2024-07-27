"""
U.S. States Game

This Python script creates a game where the user guesses U.S. states based on their locations on a map. The game uses the `turtle` library to display a map and prompts the user to input state names. Correctly guessed states are displayed on the map.

How it works:
1. Sets up the turtle graphics window and loads a map image.
2. Prompts the user to guess state names in a loop until 50 guesses are made or the user cancels the input.
3. Checks if the guessed state is valid and not previously guessed.
4. Displays the guessed state on the map at the corresponding coordinates.
5. Provides feedback for invalid or duplicate guesses.
6. Prints the list of correctly guessed states and any remaining unguessed states after the game ends.

Requirements:
- Python 3.x
- pandas
- turtle (standard library)

File Dependencies:
- `50_states.csv`: A CSV file with columns `state`, `x`, and `y` for state names and their coordinates.
- `world_map.gif`: An image file of the world map used for display.

Usage:
1. Ensure `50_states.csv` and `world_map.gif` are in the same directory as this script.
2. Run the script using Python.

Example:
```bash
python main.py
"""

import pandas as pd
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "world_map.gif"
screen.addshape(image)
turtle.shape(image)


def guess_state(guess):
    return screen.textinput(title=f"Guess the state {guess}/50", prompt="Enter the state's name: ").title()

data = pd.read_csv("50_states.csv")
data.set_index('state', inplace=True)
states_list = data.index.tolist()

guess = 0
correct_guesses = []


while guess < 50:
    answer_state = guess_state(guess)
    if answer_state == "":  
        break
    if answer_state in states_list and answer_state not in correct_guesses:
        guess += 1
        correct_guesses.append(answer_state)
        x_coordinate = data.loc[answer_state, 'x']
        y_coordinate = data.loc[answer_state, 'y']
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x_coordinate, y_coordinate)
        t.write(answer_state)
    else:
        if answer_state not in states_list:
            print(f"{answer_state} is not a valid state name.")
        elif answer_state in correct_guesses:
            print(f"{answer_state} has already been guessed.")


print("Correct guesses:", correct_guesses)
unguessed_states = [state for state in states_list if state not in correct_guesses]
print("Unguessed states:", unguessed_states)

turtle.done()

