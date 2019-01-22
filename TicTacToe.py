from random import randint
""""
Simple TicTacToe Game used as a challenge for myself to further develop my understanding and programming language with Python
Author: Stanley Ho
"""
board = [["     1 ", " 2 ", " 3 "],
         [" 1 ", "[ ]", "[ ]", "[ ]"],
         [" 2 ", "[ ]", "[ ]", "[ ]"],
         [" 3 ", "[ ]", "[ ]", "[ ]"]]

possibleMoves = [[1, 1], [1, 2], [1, 3], [2, 1],
                 [2, 2], [2, 3], [3, 1], [3, 2], [3, 3]]

# Function to print the board without " " being present


def print_board(board):
    for row in board:
        print(" ".join(row))


# Function defining the rules of the game
def winner(board, letter):
    return ((board[1][1] == letter and board[1][2] == letter and board[1][3] == letter) or  # across the top
            # across the middle
            (board[2][1] == letter and board[2][2] == letter and board[2][3] == letter) or
            # across the bottom
            (board[3][1] == letter and board[3][2] == letter and board[3][3] == letter) or
            # across the left side
            (board[1][1] == letter and board[2][1] == letter and board[3][1] == letter) or
            # across the middle
            (board[1][2] == letter and board[2][2] == letter and board[3][2] == letter) or
            # across the right side
            (board[1][3] == letter and board[2][3] == letter and board[3][3] == letter) or
            # top left diagonal
            (board[1][1] == letter and board[2][2] == letter and board[3][3] == letter) or
            (board[1][3] == letter and board[2][2] ==
             letter and board[3][1] == letter)  # top right diagonal
            )
# Function to define a valid move


def valid_move(move):
    if move == "[X]" or move == "[O]":
        return False
    else:
        return True


print("Welcome to Tic-Tac-Toe. Can you beat the computer? Lets see.")

# Print the board for the player to See
print_board(board)

# Play the game while there are possible moves
for turn in range(0, len(possibleMoves)):

    if len(possibleMoves) > 0:
        if winner(board, "[X]"):
            print("You Won")
            print_board(board)
            break
        elif winner(board, "[O]"):
            print("Sorry you lose!")
            print_board(board)
            break
        player_row = int(input("Input row: "))
        player_col = int(input("Input column: "))
        if player_row < 1 or player_row > 3 or player_col < 1 or player_row > 3:
            print("Please enter a valid move between 1-3")
        else:

            if valid_move(board[player_row][player_col]) is True:
                comp_move = randint(0, len(possibleMoves)-1)
                board[player_row][player_col] = "[X]"
                possibleMoves.remove([player_row, player_col])
                if len(possibleMoves) == 0:
                    print("Draw")
                else:
                    # Makes the computer pick a random index out of a list of possible moves
                    comp_move = randint(0, len(possibleMoves) - 1)
                    # Get the move from the list using the random index
                    computer_move = possibleMoves[comp_move]
                    print("Computer placed O at: " + str(computer_move))
                    # Changes the board to [O] using the index
                    board[computer_move[0]][computer_move[1]] = "[O]"
                    possibleMoves.remove([computer_move[0], computer_move[1]])

            else:
                print("Move not valid Position already taken please choose another")

            print_board(board)
