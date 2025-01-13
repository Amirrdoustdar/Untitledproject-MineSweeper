import random

def create_board(n, m, bombs):
    board = [[0 for _ in range(m)] for _ in range(n)]
    for x, y in bombs:
        board[x][y] = '*'
    return board

def update_board_with_counts(board, n, m):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for x in range(n):
        for y in range(m):
            if board[x][y] == '*':
                continue
            count = 0
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == '*':
                    count += 1
            board[x][y] = count

def print_board(board, revealed):
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if revealed[i][j]:
                print(cell, end=' ')
            else:
                print('#', end=' ')
        print()

def generate_bombs(n, m, k):
    positions = set()
    while len(positions) < k:
        x, y = random.randint(0, n - 1), random.randint(0, m - 1)
        positions.add((x, y))
    return positions

def uncover_cell(board, revealed, x, y):
    if board[x][y] == '*':
        print("Boom! You hit a bomb.")
        return True
    
    revealed[x][y] = True
    if board[x][y] == 0:
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and not revealed[nx][ny]:
                uncover_cell(board, revealed, nx, ny)
    return False

def main():
    print("Select difficulty level:")
    print("1. Easy (5x5, 5 bombs)")
    print("2. Medium (10x10, 20 bombs)")
    print("3. Hard (15x15, 40 bombs)")
    
    try:
        choice = int(input("Enter your choice (1-3): "))
        if choice == 1:
            n, m, k = 5, 5, 5
        elif choice == 2:
            n, m, k = 10, 10, 20
        elif choice == 3:
            n, m, k = 15, 15, 40
        else:
            print("Invalid choice. Defaulting to Easy.")
            n, m, k = 5, 5, 5

        bombs = generate_bombs(n, m, k)
        board = create_board(n, m, bombs)
        update_board_with_counts(board, n, m)
        
        revealed = [[False for _ in range(m)] for _ in range(n)]
        
        while True:
            print_board(board, revealed)
            try:
                x, y = map(int, input("Enter cell to uncover (row col): ").split())
                if x < 1 or x > n or y < 1 or y > m:
                    print("Invalid coordinates. Try again.")
                    continue
                
                if uncover_cell(board, revealed, x - 1, y - 1):
                    print_board(board, [[True for _ in range(m)] for _ in range(n)])
                    print("Game Over!")
                    break
                
                if all(revealed[i][j] or board[i][j] == '*' for i in range(n) for j in range(m)):
                    print("Congratulations! You've cleared the board.")
                    break
            except ValueError:
                print("Invalid input. Enter row and column as integers.")
                continue

    except ValueError:
        print("Invalid input. Exiting game.")

if __name__ == "__main__":
    main()
