import random

word_list = ["aardvark", "baboon", "camel","mouse"]

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


secret_word = list(random.choice(word_list))
guessed_letters = []
attempts = 0
game_over = False

def draw_guesses(secret_word,guessed_letters):
  for i in secret_word:
    if i == guessed_letters :
      print(i, end=' ') 
    else:
      print('_', end=' ') 

def findingletter(letter,secret_word):
    for i in secret_word:
      if i == letter:
        return True
      return False
      
def draw_hang(attempts):
  if attempts < len(HANGMANPICS):
    print(HANGMANPICS[attempts])
  else:
    game_over = True
    return game_over

while game_over == False:
    user_guess = input('\nGuess a letter: ')
    coincidence = findingletter(user_guess)
    if coincidence:
      guessed_letters.append(user_guess)
      draw_guesses(secret_word,guessed_letters)
      print('')
      draw_hang(attempts)
    else:
      print(f"You guessed {user_guess}, that's not in the word you loose a life")
      draw_guesses(secret_word,guessed_letters)
      print('')
      attempts+=1
      draw_hang(attempts)

