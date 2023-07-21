board = [[' ' for j in range(3)] for i in range(3)]

gameOver = False

player = 'X'


def printBoard(board):
    for i in range(3):
        print('|', end="")
        for j in range(3):
            print(board[i][j], end="|")
        print()


def haveWon(board, player):
    # check rows
    for i in range(3):
        if (board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != ' '):
            return True
    # check columns
    for i in range(3):
        if (board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != ' '):
            return True
    # Check diagonals
    if (board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != ' '):
        return True
    if (board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != ' '):
        return True
    return False


def turn(board):
    x, o = 0, 0
    for row in board:
        for element in row:
            if element == "X":
                x += 1
            elif element == 'O':
                o += 1

    if (x > o):
        return "O"
    elif x == o:
        return "X"
    else:
        return ""


printBoard(board)
while (not gameOver):
    print(f"Enter your move player {player}: ")
    row = int(input())
    col = int(input())
    if (board[row][col] == ' '):
        board[row][col] = player
        gameOver = haveWon(board, player)
        if gameOver:
            print(f"Player {player} has won!")
            break
        else:
            if player == 'X':
                player = 'O'
            else:
                player = 'X'

    else:
        print("Invalid move")
    printBoard(board)
    print(turn(board))
