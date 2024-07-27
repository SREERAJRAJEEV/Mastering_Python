# U.S. States Game

## Overview

The U.S. States Game is a Python application where users guess U.S. states based on a map. The game uses the `turtle` library to display a world map and prompts users to input state names. Correct guesses are shown on the map at their respective coordinates.

## Features

- Displays a map using turtle graphics.
- Prompts the user to guess U.S. states.
- Shows correctly guessed states on the map.
- Provides feedback for invalid or previously guessed states.
- Lists unguessed states after the game ends.

## Repository Structure

The project is organized as follows:

```
Mastering_Python/
├── Mastering_Pandas/
│   └── US_State_Guessing_Games/
│       ├── us_states_game.py
│       ├── 50_states.csv
│       └── world_map.gif
```

## Requirements

- Python 3.x
- pandas
- turtle (standard library)

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/SREERAJRAJEEV/Mastering_Python.git
   cd Mastering_Python/Mastering_Pandas/US_State_Guessing_Games
   ```

2. **Install Dependencies**

   Install the required Python package using pip:

   ```bash
   pip install pandas
   ```

3. **Prepare Assets**

   Ensure the following files are in the `US_State_Guessing_Games` directory:

   - **Map Image**: `world_map.gif` - Used for displaying the map in the turtle graphics window.
   - **CSV File**: `50_states.csv` - Contains state names and coordinates. The CSV should have the following columns:
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


## Contributing

Feel free to fork this repository, make changes, and submit a pull request. Contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
