N = 8
# Create empty board
board = [[0 for _ in range(N)] for _ in range(N)]
# Function to print board
def print_board():
 print("\nCurrent Board:\n")
 for i in range(N):
 for j in range(N):
 if board[i][j] == 1:
 print("Q", end=" ")
 else:
 print(".", end=" ")
 print()
# Check if safe
def is_safe(row, col):
 # Check row
 for i in range(N):
 if board[row][i] == 1:
 return False
 # Check column
 for i in range(N):
 if board[i][col] == 1:
 return False
 # Check diagonals
 for i in range(N):
 for j in range(N):
 if board[i][j] == 1:
 if abs(i - row) == abs(j - col):
 return False
 return True
# User places 8 queens
count = 0
while count < 8:
 print_board()

 row = int(input("Enter row (0-7): "))
 col = int(input("Enter column (0-7): "))
 if row < 0 or row >= N or col < 0 or col >= N:
 print("Invalid position! Try again.")
 continue
 if is_safe(row, col):
 board[row][col] = 1
 count += 1
 print("Queen placed successfully!")
 else:
 print("Not safe position! Try again.")
print("\nAll 8 Queens placed successfully!")
print_board()
