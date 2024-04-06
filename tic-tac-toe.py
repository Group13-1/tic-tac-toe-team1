def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if board[0][0] == board[1][1] == board[2][2] == player:
        return True

    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

def play_tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    for _ in range(9):
        row, col = map(int, input(f"Player {current_player}, enter row and column (1-3): ").split())
        row -= 1
        col -= 1

        if board[row][col] != " ":
            print("Cell already taken. Try again.")
            continue

        board[row][col] = current_player
        print_board(board)

        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break

        current_player = "O" if current_player == "X" else "X"
    else:
        print("It's a tie!")

if __name__ == "__main__":
    play_tic_tac_toe()
