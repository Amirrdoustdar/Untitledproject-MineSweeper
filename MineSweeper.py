def print_minesweeper(n, m, bombs):
    # ایجاد یک صفحه n * m با مقدار اولیه 0
    board = [[0 for _ in range(m)] for _ in range(n)]

    # تغییر خانه‌های حاوی بمب به '*'
    for x, y in bombs:
        board[x-1][y-1] = '*'
    
    # بررسی خانه‌های اطراف هر بمب
    for x, y in bombs:
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x - 1 + dx, y - 1 + dy
                # اطمینان حاصل کنید که از محدوده جدول خارج نشویم
                if 0 <= nx < n and 0 <= ny < m and board[nx][ny] != '*':
                    board[nx][ny] += 1
    
    # چاپ نتیجه
    for row in board:
        print(' '.join(map(str, row)))

# ورودی
n, m = map(int, input().split())  # تعداد سطرها و ستون‌ها
k = int(input())  # تعداد بمب‌ها

bombs = [tuple(map(int, input().split())) for _ in range(k)]  # موقعیت بمب‌ها

# فراخوانی تابع
print_minesweeper(n, m, bombs)
