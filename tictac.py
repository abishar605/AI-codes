# Tic Tac Toe using 2D Array
# Create 3x3 board
board = [[" " for _ in range(3)] for _ in range(3)]
# Print board
def print_board():
 print("\nBoard:")
 for i in range(3):
 print(" | ".join(board[i]))
 print("-" * 9)
# Check winner for any player
def check_winner(player):
 # Check rows (X direction)
 for x in range(3):
 if board[x][0] == board[x][1] == board[x][2] == player:
 return True
 # Check columns (Y direction)
 for y in range(3):
 if board[0][y] == board[1][y] == board[2][y] == player:
 return True
 # Check diagonals
 if board[0][0] == board[1][1] == board[2][2] == player:
 return True
 if board[0][2] == board[1][1] == board[2][0] == player:
 return True
 return False
# Check draw
def check_draw():
 for x in range(3):
 for y in range(3):
 if board[x][y] == " ":
 return False
 return True
# Main game
def tic_tac_toe():
 player = "X"
 print("TIC TAC TOE USING 2D ARRAY (X,Y)")
 print("Enter row (X) and column (Y) between 0 and 2")
 while True:
 print_board()
 # Input
 x = int(input(f"Player {player} Enter X (0-2): "))
 y = int(input(f"Player {player} Enter Y (0-2): "))
 # Validate input
 if x < 0 or x > 2 or y < 0 or y > 2:
 print("Invalid position! Enter values between 0 and 2")
 continue
 # Check already filled
 if board[x][y] != " ":
 print("Position already filled!")
 continue
 # Place mark
 board[x][y] = player
 # Check winner (for X or O)
 if check_winner(player):
 print_board()
 print(f"Player {player} WINS!")
 break
 # Check draw
 if check_draw():
 print_board()
 print("GAME DRAW!")
 break
 # Switch player
 if player == "X":
 player = "O"
 else:
 player = "X"
# Run game
tic_tac_toe()
