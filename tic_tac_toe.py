import math

board = [" " for _ in range(9)]

def print_board():
    print()
    for i in range(3):
        print(" | ".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("-" * 9)
    print()

def show_positions():
    print("Board Positions:")
    print("1 | 2 | 3")
    print("-" * 9)
    print("4 | 5 | 6")
    print("-" * 9)
    print("7 | 8 | 9")
    print()

def winner(player):
    wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]

    for combo in wins:
        if all(board[i] == player for i in combo):
            return True
    return False

def draw():
    return " " not in board

def minimax(is_ai):

    if winner("O"):
        return 1

    if winner("X"):
        return -1

    if draw():
        return 0

    if is_ai:

        best = -100

        for i in range(9):

            if board[i] == " ":

                board[i] = "O"

                score = minimax(False)

                board[i] = " "

                best = max(best, score)

        return best

    else:

        best = 100

        for i in range(9):

            if board[i] == " ":

                board[i] = "X"

                score = minimax(True)

                board[i] = " "

                best = min(best, score)

        return best

def ai_move():

    best_score = -100
    move = -1

    for i in range(9):

        if board[i] == " ":

            board[i] = "O"

            score = minimax(False)

            board[i] = " "

            if score > best_score:

                best_score = score
                move = i

    board[move] = "O"

def player_move():

    while True:

        try:

            move = int(input("Choose position (1-9): ")) - 1

            if move < 0 or move > 8:
                print("Invalid position")
                continue

            if board[move] == " ":

                board[move] = "X"
                break

            else:
                print("Already occupied")

        except:
            print("Enter a number")

print("="*50)
print("🎮 TIC TAC TOE AI")
print("You = X")
print("AI = O")
print("="*50)

show_positions()

while True:

    print_board()

    player_move()

    if winner("X"):

        print_board()
        print("🎉 You Win!")
        break

    if draw():

        print_board()
        print("🤝 Draw!")
        break

    print("🤖 AI thinking...")

    ai_move()

    if winner("O"):

        print_board()
        print("🤖 AI Wins!")
        break

    if draw():

        print_board()
        print("🤝 Draw!")
        break
