# Imports all the game files
import hangman
import madlibs
import ticTacToe

# Menu to display game options 
def menu():
  print("Welcome to the Beach Arcade! What would you like to do?")
  print("1. Play Hangman ")
  print("2. Play Tic-Tac-Toe")
  print("3. Play Madlibs")
  print("4. Quit" ) 

# validates that the input is an int
def validInput(range1, range2):
  while True:
    try:
      num = int(input("Enter a number: "))
      
      if num >= range1 and num <= range2:
        break
      
      
      print(f"Number has to be in the range of {range1} to {range2}!")
    
    # Throws an error if its not an integer input.
    except ValueError:
      print("Invalid input!")

  return num
  
def main():
  selection = 0

# Will continuosuly loop allowing the user to play multiple games until they quit by entering 4
  while selection != 4: 
    menu()

    selection = validInput(1, 4)
     
    if selection == 1:
      
      Hangman.main()
    elif selection == 2:
      
      TicTacToe.main()
    elif selection == 3:
      
      Madlibs.main()

    else:
      print("Thanks for playing!")
  

main()


