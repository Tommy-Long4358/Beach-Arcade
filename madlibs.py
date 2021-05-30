def menu():
  print("\nWelcome to Madlibs!")
  print("1. Load first madlib")
  print("2. Load second madlib")
  print("3. Quit")

def madlib1():
  # display string 
  print("\nToday was the best day! I went with my friend _____ (1) to the beach. As soon as we got to the beach, we decided to build a _____ (2) sandcastle that looked like a _____ (3). After playing in the sand, we know we had to cool off in the water. I took my _____ (4) _____ (5) into the water. _____ (6) and i waited for a _____ (7) wave. While wading out in the _____ (8) water, I felt something _____ (9) brush against my leg. I began to _____ (10) and froze with fear. I could not move. Then, _____ (11) began to _____ (12) when he/she saw what touched my leg. Whew...It was only a _____ (13). Going to the beach is always an adventure!")
  
  # user inputs 
  print("\nPlease enter a word to fill in the following prompts")
  one = input("1. Friend's name: ")
  two = input("2. Adjective: ")
  three = input("3. Noun: ")
  four = input("4. Adjective: ")
  five = input("5. Noun: ")
  six = input("6. Friend's name: ")
  seven = input("7. Adjective: ")
  eight = input("8. Adjective: ")
  nine = input("9. Adjective: ")
  ten = input("10. Verb: ")
  eleven = input("11. Friend's name: ")
  tweleve = input("12. Verb: ")
  thriteen  = input("13. Noun: ")

  print(f"\nToday was the best day! I went with my friend {one} to the beach. As soon as we got to the beach, we decided to build a {two} sandcastle that looked like a {three}. After playing in the sand, we know we had to cool off in the water. I took my {four} {five} into the water. {six} and i waited for a {seven} wave. While wading out in the {eight} water, I felt something {nine} brush  against my leg. I began to {ten} and froze with fear. I could not move. Then, {eleven} began to {tweleve} when he/she saw what touched my leg. Whew...It was only a {thriteen}. Going to the beach is always an adventure!\n")


def madlib2():
  # display string
  print("\nSummer trips to the beach are so _____ (1)! Pack your _____ (2) ,a _____ (3) to dry yourself off, and _____ (4) to prevent sunburn. Be sure to bring a _____ (5) to _____ (6) with in the water, too. You can bring a beach picnic, with _____ (7), _____ (8), and _____ (9) to drink. It's fun to _____ (10) for hours in the water, and to see _____ (11) sail past in the distance.")
  
  #User inputs 
  print("\nPlease enter a word to fill in the following prompts:")
  one = input("1. Adjective: ")
  two = input("2. Noun; Clothing: ")
  three = input("3. Noun: ")
  four = input("4. Noun: ")
  five = input("5. Noun: ")
  six = input("6. Verb: ")
  seven = input("7. Noun; Food: ")
  eight = input("8. Noun; Food: ")
  nine = input("9. Noun; Drink: ")
  ten = input("10. Verb: ")
  eleven = input("11. Plural noun: ")

  print(f"\nSummer trips to the beach are so {one}! Pack your {two} ,a {three} to dry yourself off, and {four} to prevent sunburn. Be sure to bring a {five} to {six} with in the water, too. You can bring a beach picnic, with {seven}, {eight}, and {nine} to drink. It's fun to {ten} for hours in the water, and to see {eleven} sail past in the distance.\n")

def validInput(range1, range2):
  while True:
    try:
      num = int(input("Enter a number: "))
      
      if num >= range1 and num <= range2:
        break
      
      print(f"Number has to be in the range of {range1} to {range2}!")
    except ValueError:
      print("Invalid input!")

  return num

def main():
  choice = 0

  while choice != 3:
    menu()  
    choice = validInput(1, 3)
    
    if choice == 1:
      madlib1()

    elif choice == 2:
      madlib2()

    else: 
      print("\nThanks for playing Madlibs!\n")
      break
    
    
  
