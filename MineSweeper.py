def print_minesweeper(n, m, bombs):
   
    board = [[0 for _ in range(m)] for _ in range(n)]

   
    for x, y in bombs:
        board[x-1][y-1] = '*'
    
    
    for x, y in bombs:
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x - 1 + dx, y - 1 + dy
                
                if 0 <= nx < n and 0 <= ny < m and board[nx][ny] != '*':
                    board[nx][ny] += 1
    
    
    for row in board:
        print(' '.join(map(str, row)))


n, m = map(int, input().split())  
k = int(input())  

bombs = [tuple(map(int, input().split())) for _ in range(k)]  


print_minesweeper(n, m, bombs)
