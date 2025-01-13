# Minesweeper Game

A simple console-based implementation of the Minesweeper game in Python.

## Features

- **Customizable Board Size:** Specify the number of rows and columns for the game board.
- **User-defined Bomb Locations:** Place bombs by entering their coordinates.
- **Automatic Hint Generation:** The board is updated with numbers indicating the count of adjacent bombs.
- **Input Validation:** Ensures user inputs are within valid ranges and formats.
- **Clear Output:** Displays the board in a readable format.

## How It Works

1. **Input:**
   - Enter the number of rows and columns for the game board.
   - Specify the number of bombs and their coordinates.
2. **Processing:**
   - The program creates a board with bombs and updates cells with the number of adjacent bombs.
3. **Output:**
   - A visual representation of the Minesweeper board.

## Code Overview

### Key Functions:

1. **`create_board(n, m, bombs)`**
   - Initializes the game board and places bombs.
2. **`update_board_with_counts(board, n, m, bombs)`**
   - Updates the board with the count of adjacent bombs for each cell.
3. **`print_board(board)`**
   - Prints the board in a user-friendly format.
4. **`validate_input(n, m, k, bombs)`**
   - Ensures that input dimensions, bomb count, and bomb locations are valid.

### Main Function:

- **`main()`**
  - Handles user input, validates it, generates the game board, and displays the output.

## Running the Program

1. Ensure Python 3.x is installed on your system.
2. Save the code in a file named `minesweeper.py`.
3. Open a terminal or command prompt and navigate to the directory containing the file.
4. Run the program with:
   ```bash
   python minesweeper.py
   
License
This project is licensed under the MIT License.

You are free to:

Use the code for personal or commercial projects.
Modify the code to suit your needs.
Distribute your own version of the code.
However, you must include the original license text in any copies or substantial portions of the project. The software is provided "as is," without warranty of any kind.
