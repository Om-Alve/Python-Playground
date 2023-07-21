board = list(map(int, input().split(" ")))

max = max(board)

for num in board:
    if num != max:
        print(max-num, end=" ")
