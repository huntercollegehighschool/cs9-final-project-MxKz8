"""
Name(s): Ellie, Kyle
Name of Project: EK HANGING
"""

import os
from random import choice
from p1wordbank import wordList
from p2image import victim, title

print(title)
print("Owners: Ellie, Kyle")
print("Project: EK HANGING")
nickname = input("Enter a nickname: ")

print("Hello " + nickname)
print("You will have 6 lives per game.")
print("Good luck, ur going to need it!")

def playerGuess(word: str, guessedLetters: list):
  global lives
  guess = input("\n\nGuess a letter: ").upper()
  msg = ''
  if not guess.isalpha():
    msg = "My guy, you sure we playing the same game?"
  elif guess in guessedLetters:
    msg = nickname + ", my guy, you already guessed that. smh."
  else:
    guessedLetters.append(guess)
    if guess in word:
      msg = "Lucky guess smh"
    else:
      lives -= 1
      msg = "W R O N G"
  bigprint(guessedLetters, msg)


def bigprint(guessedLetters, msg):
  os.system('clear')
  print(title + '\nOwners: Ellie, Kyle\nProject: EK HANGING\nNickname: ' + nickname + '\nHello ' + nickname + '. We believe you are too unintelligent to win this masterpiece of a hanging. Prove us wrong.' + victim[lives] + '           ' + ' '.join([letter if letter in guessedLetters else ' ' if letter == ' ' else '_' for letter in word]) + '            Wrong: ' + ' '.join([letter for letter in guessedLetters if letter not in word]) + '\n' + msg)

def game():
  global lives, word
  word = choice(wordList)
  guessedLetters = []
  lives = 6

  bigprint(guessedLetters, '')
  while True:
    playerGuess(word, guessedLetters)
    if lives <= 0 or len([letter for letter in word if letter not in guessedLetters and letter != ' ']) <= 0:
      break


game()
while True:
  print(('As we expected, you are below us. The word was ' + word + '.\n') if lives <= 0 else 'Hmm. Perhaps you deserve more credit. \n')
  if input('Would you like to lose again? (Y/N)\n').upper() == 'Y':
    game()
  else:
    break