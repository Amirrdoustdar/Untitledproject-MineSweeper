def create_board(n, m, bombs):
    """
    Create a Minesweeper board with the given dimensions and bomb locations.
    
    :param n: Number of rows in the board.
    :param m: Number of columns in the board.
    :param bombs: List of tuples representing bomb coordinates.
    :return: A 2D list representing the Minesweeper board.
    """
    board = [[0 for _ in range(m)] for _ in range(n)]
    
    for x, y in bombs:
        if 0 <= x-1 < n and 0 <= y-1 < m:
            board[x-1][y-1] = '*'
    
    return board

def update_board_with_counts(board, n, m, bombs):
    """
    Update the board with the count of adjacent bombs for each cell.
    
    :param board: The Minesweeper board.
    :param n: Number of rows in the board.
    :param m: Number of columns in the board.
    :param bombs: List of tuples representing bomb coordinates.
    """
    for x, y in bombs:
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x - 1 + dx, y - 1 + dy
                if 0 <= nx < n and 0 <= ny < m and board[nx][ny] != '*':
                    board[nx][ny] += 1

def print_board(board):
    """
    Print the Minesweeper board in a user-friendly format.
    
    :param board: The Minesweeper board to print.
    """
    for row in board:
        print(' | '.join(map(str, row)))
        print('-' * (4 * len(row) - 1))

def validate_input(n, m, k, bombs):
    """
    Validate the input values for the Minesweeper game.
    
    :param n: Number of rows in the board.
    :param m: Number of columns in the board.
    :param k: Number of bombs.
    :param bombs: List of tuples representing bomb coordinates.
    :return: True if the input is valid, False otherwise.
    """
    if n <= 0 or m <= 0:
        print("Error: Board dimensions must be positive.")
        return False
    if k < 0 or k > n * m:
        print("Error: Number of bombs must be between 0 and the total number of cells.")
        return False
    for x, y in bombs:
        if x < 1 or x > n or y < 1 or y > m:
            print(f"Error: Bomb at ({x}, {y}) is out of bounds.")
            return False
    return True

def main():
    """
    Main function to run the Minesweeper game.
    """
    try:
        n, m = map(int, input("Enter the number of rows and columns (n m): ").split())
        k = int(input("Enter the number of bombs (k): "))
        bombs = [tuple(map(int, input(f"Enter bomb {i+1} coordinates (x y): ").split())) for i in range(k)]
        
        if not validate_input(n, m, k, bombs):
            return
        
        board = create_board(n, m, bombs)
        update_board_with_counts(board, n, m, bombs)
        print_board(board)
    
    except ValueError:
        print("Error: Invalid input format. Please enter integers.")

if __name__ == "__main__":
    main()
