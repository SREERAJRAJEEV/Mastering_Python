# U.S. States Game

## Overview

The U.S. States Game is a Python application where users guess U.S. states based on a map. The game uses the `turtle` library to display a world map and prompts users to input state names. Correct guesses are shown on the map at their respective coordinates.

## Features

- Displays a map using turtle graphics.
- Prompts the user to guess U.S. states.
- Shows correctly guessed states on the map.
- Provides feedback for invalid or previously guessed states.
- Lists unguessed states after the game ends.

## Requirements

- Python 3.x
- pandas
- turtle (standard library)

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/us-states-game.git
   cd us-states-game
   ```

2. **Install Dependencies**

   Install the required Python package using pip:

   ```bash
   pip install pandas
   ```

3. **Prepare Assets**

   - **Map Image**: Ensure you have the `world_map.gif` image file in the project directory. This image is used for displaying the map in the turtle graphics window. You can download or create your own map image.
   - **CSV File**: Make sure the `50_states.csv` file is in the project directory. This CSV file should have the following columns:
     - `state`: Name of the state
     - `x`: x-coordinate for the state location on the map
     - `y`: y-coordinate for the state location on the map

   Example CSV format:

   ```csv
   state,x,y
   Alabama,30,-86
   Alaska,61,-150
   ...
   ```

## Usage

1. **Run the Script**

   Execute the script using Python:

   ```bash
   python us_states_game.py
   ```

2. **Play the Game**

   - A turtle graphics window will appear with the world map.
   - Enter state names when prompted. The game will display the state on the map if the guess is correct.
   - After making up to 50 guesses or if the user cancels the input, the game will print the list of correct guesses and any unguessed states.

## Code Example

```python
import pandas as pd
import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "world_map.gif"
screen.addshape(image)
turtle.shape(image)

# Function to prompt user for a state guess
def guess_state(guess):
    return screen.textinput(title=f"Guess the state {guess}/50", prompt="Enter the state's name: ").title()

# Read the CSV file into a DataFrame and set the 'state' column as the index
data = pd.read_csv("50_states.csv")
data.set_index('state', inplace=True)
states_list = data.index.tolist()

# Initialize guess count and correct guesses list
guess = 0
correct_guesses = []

# Main game loop
while guess < 50:
    answer_state = guess_state(guess)
    if answer_state == "":  # Check if user clicked cancel or input is empty
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

# Print correct guesses and remaining states
print("Correct guesses:", correct_guesses)
unguessed_states = [state for state in states_list if state not in correct_guesses]
print("Unguessed states:", unguessed_states)

# Keep the turtle graphics window open
turtle.done()
```

## Contributing

Feel free to fork this repository, make changes, and submit a pull request. Contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

This format should ensure that headings, code blocks, and other elements display properly on GitHub and other Markdown viewers.
