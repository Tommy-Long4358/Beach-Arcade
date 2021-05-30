import random
from words import words
import string

class HangmanGame:
  def __init__(self): 
    self.attempts = 0
    self.hidden_word = "-"
    self.user_letter = " "
    self.lettersDict = {}

  # Displays options for hangman 
  def menu(self):
    print("\nWelcome to Hangman!")
    print("1. Play ")
    print("2. Quit" )   

  # Track the number of attempt 
  def attempt_tracker(self, max_attempt):
    
    self.attempts += 1 
    print("Attempt: ", self.attempts, "/", max_attempt, "\n")

  # Word display - prints out the word  
  def word_display(self, word, user_letter):
    # makes dictionary of letters equal to false
    if len(self.lettersDict) == 0:
      for i in range (len(word)): 
        self.lettersDict[word[i].upper()] = False 

    # sets dictionary value to true if guessed
    if user_letter in self.lettersDict:
      self.lettersDict[user_letter] = True
    
    # creates string of guessed words
    letters_in_word = list(word.upper())
    displayed_word = ""
    for letter in letters_in_word:
      if self.lettersDict[letter] == True:
        displayed_word += letter
      else:
        displayed_word += "-"

    return displayed_word
      
    
  # logic for hangman, incorporates previous functions  
  def hangman(self):
    
    # Chooses a random word from the list
    word = random.choice(words)
    max_attempts = len(word) * 2
    
    word_letters = set(word.upper()) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # What the user has guessed
    
    # loops as long as word is longer than 0 
    while len(word_letters) > 0:
      # Getting user input
      self.user_letter = input("\nGuess a letter: " ).upper()
      
      # If the user input is not guessed yet, add it to used_letters set 
      if self.user_letter in alphabet - used_letters: 
        used_letters.add(self.user_letter)
        
        # If the user input is guessed correctly
        if self.user_letter in word_letters: 
          
          # Remove the correct letter from the remaining possible list of letters.
          word_letters.remove(self.user_letter)

          print("\nYou guessed the letter right!")
          
      
        else:

          # If user guesses wrong letter, attempts is incremented.
          self.attempt_tracker(max_attempts)
          
        
        print(self.word_display(word, self.user_letter))
        
        # Game stops once the user has reached the max amount of attempts.
        if self.attempts == max_attempts:
          print("\nYou lose!")
          print("The word was:", word.upper(),"\n")
          break

      
      elif self.user_letter in used_letters:
        print('\nThis letter is already guessed. Please try again!')
      
      else: 
        print("Invalid character. Please try again.")

      # User wins if all letters are guessed and its below the max attempts available.
      if len(word_letters) == 0 and self.attempts < max_attempts:
        print("\nYou won!")
        print("The word was:", word.upper(), "\n")
        break

# Function to check for valid input.
def validInput(range1, range2):
  while True:
    try:
      num = int(input("Enter a number: "))
      
      # If statement that goes out of the while loop once it finds a valid number.   
      if num == range1 or num == range2:
        break
      
      print(f"Number has to be in the range of {range1} to {range2}!")
    except ValueError:
      print("Invalid input!")

  return num


def main():
  hang = HangmanGame()

  choice = 0
  
  while choice == 0:
    hang.menu()
    choice = validInput(1, 2)

    if choice == 1:
      hang.hangman()
      
    
    else:
      print("\nThanks for playing Hangman!\n")
      break
    
    

