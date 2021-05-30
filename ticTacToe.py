# TIC-TAC-TOE
import random 

# TODO: Make a more accurate valid input checker
class TicTacToe:
  def __init__(self):
    self.player1 = 1
    self.player2 = 0
    self.bot = 0
    self.board = [[3, 3, 3], [3, 3, 3], [3, 3, 3]] 
    self.currentPlayer = 1 
    
  # Function that determines who goes first in a Tic-Tac-Toe game.
  def turnChooser(self):
    turn = random.randint(0, 1)

    return turn

  # Function that displays the board.
  def displayBoard(self, board):

    # Double for loop that goes through the board and puts in X's and O's at designated spots provided by user or bot.
    for i in range(len(self.board)):
      for j in range(len(self.board[i])):
        if self.board[i][j] == 3:
          print(".", end = "")
          
        elif self.board[i][j] == 1:
          print("x", end = "")
        
        elif self.board[i][j] == 0:
          print("o", end = "")
          
      print()

  # Function that checks for the winner based on the patterns of 3 in a row, diagonally, or columns.
  def checkWinner(self, board):
    # row
    if self.board[0][0] == self.board[0][1] == self.board[0][2] != 3:
      return True 

    elif self.board[1][0] == self.board[1][1] == self.board[1][2] != 3:
      return True 

    elif self.board[2][0] == self.board[2][1] == self.board[2][2] != 3:
      return True 
    
    # column
    elif self.board[0][0] == self.board[1][0] == self.board[2][0] != 3:
      return True 

    elif self.board[0][1] == self.board[1][1] == self.board[2][1] != 3:
      return True 

    elif self.board[0][2] == self.board[1][2] == self.board[2][2] != 3:
      return True 
    
    # diagonal
    elif self.board[0][0] == self.board[1][1] == self.board[2][2] != 3:
      return True 

    elif self.board[0][2] == self.board[1][1] == self.board[2][0] != 3:
      return True 

    else:
      return False
  
  # Function that resets the board back to normal after each game.
  def resetBoard(self):
    self.board = [[3, 3, 3], [3, 3, 3], [3, 3, 3]]  

  # Function that takes in input for the row and column the user wants to put in.
  def playerTurn(self, player):

    # Input is subtracted by 1 to account for index. It's needed for user to put rows and columns at 1.
    r = int(input("Choose a row: " )) - 1 
    c = int(input("Choose a column: " )) - 1 

    # Check for invalid input like out of bounds or non-empty space
    while r < 0 or r > 2 or c < 0 or c > 2 or self.board[r][c] != 3:
      print("\nThat space is already taken! Try again.")

      r = int(input("Choose a row: " )) - 1 
      c = int(input("Choose a column: " )) - 1 
      
    # Place the player's designated number in the init() function at the row and column input.   
    self.board[r][c] = player
  
  # Function that starts the game with another friend.
  def tictactoeWithFriend(self, user, second_user):
    
    print("Choosing random player to go first...")
    
    # Determine who goes first. Assign user1 and 2 based on what turnChooser picks.
    if self.turnChooser() == 1:
      user1 = user
      user2 = second_user
      print(f"{user} goes first!")

    else:
      user1 = second_user
      user2 = user
      print(f"{second_user} goes first!")
   
    # Empty board
    print("...\n...\n...")

    # For loop from 0 - 8 since there's only a maximum of 9 possible turns in the game to do.
    for i in range(9):

      # Modulo by 2 to do alternating turns.
      if i % 2 == 0: 
        print(f"\n{user1}'s turn" )
        
        self.playerTurn(self.player1)
        
      else: 
        print(f"\n{user2}'s turn" )

        self.playerTurn(self.player2)

      # Check for winner after each turn is done and before the next turn.
      if (self.checkWinner(self.board) == True):
          self.displayBoard(self.board)
          if i % 2 == 0:
            print(f"\n{user1} wins!")

          else:
            print(f"\n{user2} wins!")
            
          break
      
      self.displayBoard(self.board)

    if not self.checkWinner(self.board):
      print("\nIt's a tie!")
    
    self.resetBoard()
  
  # Function for starting the tic-tac-toe game with a bot.
  def tictactoeWithoutFriend(self, user1):
    print("...\n...\n...")

    for i in range(9):
       
      if i % 2 == 0:
        print("\nYour turn")
         
        self.playerTurn(self.player1)

        if (self.checkWinner(self.board) == True):
          self.displayBoard(self.board)
          print(f"\n{user1} wins!")
          
          break
        
      # Bot's turn 
      else:
        
        print("\nBot's turn")
        botRow = random.randint(0, 2)
        botColumn = random.randint(0, 2)

        # Bot will keep trying for new inputs until it finds an open space on the 3 x 3 tic-tac-toe grid.
        while self.board[botRow][botColumn] != 3:
          botRow = random.randint(0, 2)
          botColumn = random.randint(0, 2)
        
        self.board[botRow][botColumn] = self.bot
      
        if (self.checkWinner(self.board) == True):
          self.displayBoard(self.board)
          
          print("\nBot wins!")
    
          break

      self.displayBoard(self.board)
    
    if not self.checkWinner(self.board):
      print("\nIt's a tie!")

    self.resetBoard()

# Function to check for valid input.
def validInput(range1, range2):
  while True:
    try:
      num = int(input("Enter a number: "))

      # If statement that goes out of the while loop once it finds a valid number.      
      if num >= range1 and num <= range2:
        break
      
      print(f"Number has to be in the range of {range1} to {range2}!")
    
    # Throws an error if its not an integer input.
    except ValueError:
      print("Invalid input!")

  return num

def menu():
  tic = TicTacToe()
  choice = 0
  
  while choice != 3:
    print("\nWelcome to Tic-Tac-Toe!\n1. Play against a bot\n2. Play with a friend\n3. Quit")

    choice = validInput(1, 3)
    
    if choice == 1:
      name1 = input("\nEnter your name: ")
      tic.tictactoeWithoutFriend(name1)

    elif choice == 2:
      
      name1 = input("\nEnter your name: ")
      name2 = input("Enter your friend's name: ")
      tic.tictactoeWithFriend(name1, name2)

    else: 
      print("\nThanks for playing tic-tac-toe!\n")
      break
    

def main():
  menu()

