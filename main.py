import jokes
import hangman
import ticTacToe

user_dict = {
  "name": "",
  "age": "",
  "grade": "",
  "adult": ""
}

goodFeelings = [
    "happy", "delighted", "great", "okay", "good", "well", "nice", "alright",
    "fine"
]

badFeelings = ["sad", "down", "depressed", "unwell", "unhappy", "bad", "bored"]

user_dict["name"] = input("Hey, I'm Sriram. What's your name? ").capitalize()

emotion = input("Hi " + user_dict["name"] + ", how are you doing? ").lower()

if len([feeling for feeling in goodFeelings if feeling in emotion]) > 0:
    print("That's Great!")
elif len([feeling for feeling in badFeelings if feeling in emotion]) > 0:
    print("That's to bad. A joke will cheer you up!")
    jokes.printJoke()
else:
    print("I bet you want to hear a joke!\nSorry in advance.")
    jokes.printJoke()

while True:
  try:
    age = input("How old are you? ").lower()
    user_dict["age"] = int(age)
    break
  except:
    print("Please input a valid number")

if user_dict["age"] < 19:
  while True:
    try:
      user_dict["grade"] = str(int(input("What grade are you in? ")))
      break
    except:
      print("Please answer with a digit")
  
  if user_dict["grade"] == "1":
    user_dict["grade"] += "st"
  elif user_dict["grade"] == "2":
    user_dict["grade"] += "nd"
  elif user_dict["grade"] == "3":
    user_dict["grade"] += "rd"
  else:
    user_dict["grade"] += "th"

  emotion = input("How is " + user_dict["grade"] + " grade going, " + user_dict["name"] + "? ").lower()

  if len([feeling for feeling in goodFeelings if feeling in emotion]) > 0:
    print("That's Great!")
  elif len([feeling for feeling in badFeelings if feeling in emotion]) > 0:
    print("That sucks")
    print("If you have any work to do maybe you should work on that.")
    print("Here's a useful article: https://www.daniel-wong.com/2018/01/30/be-successful-in-school/")
  else:
    print("I'm sure you'll do great!")
    print("Here's a useful article: https://www.daniel-wong.com/2018/01/30/be-successful-in-school/")
else:
  user_dict["adult"] = True

play_hangman = input("You want to play a quick game of hangman? (yes/no) ").lower()

while not(play_hangman == "yes" or play_hangman == "no"):
  print("Invalid Input.")
  play_hangman = input("You want to play a quick game of hangman? (yes/no) ").lower()

if play_hangman == "yes":
  hangman.startGame()

play_TicTacToe = input("You want to play a game of tic-tac-toe? (yes/no) ").lower()

while not(play_TicTacToe == "yes" or play_TicTacToe == "no"):
  print("Invalid Input.")
  play_TicTacToe = input("You want to play a quick game of hangman? (yes/no) ").lower()

if play_TicTacToe == "yes":
  ticTacToe.startGame()

while True:
  command = input('If you want to play tic-tac-toe type "!ttt". If you want to play hangman type "!hangman". If you want to quit the program type "!quit". ').lower()

  if command == "!ttt":
    ticTacToe.startGame()
  elif command == "!hangman":
    hangman.startGame()
  elif command == "!quit":
    break
  else:
    print("Invalid Input!")