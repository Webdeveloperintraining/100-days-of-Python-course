import random, hangman_art, hangman_words

chosen_word = random.choice(hangman_words.word_list)
display = []
for i in chosen_word:
    display.append('_')
attempts = 6
game_over = False

def checking_guess():
    for i in chosen_word:
        if i == guess:
            return True
    return False

def draw_guesses():
    for i in range( len(chosen_word) ):
        letter = chosen_word[i]
        if letter == guess:
            display[i]=guess
        
    for i in display:
        print(i, end = " ")
    
        
def draw_hang():
    if attempts < len(hangman_art.stages):
        print(hangman_art.stages[attempts])
   
print(hangman_art.logo)
while game_over == False:
    guess = input('\nGuess a letter: ').lower()
    while guess in display:
        print(f"\nYou've already guessed \"{guess}\" ")
        guess = input('\nPlease, guess another letter: ')
    if checking_guess() == True:
        draw_guesses()
        draw_hang()

    elif checking_guess() == False:
        print(f"You guessed {guess}, that's not in the word you loose a life")
        attempts -= 1
        draw_guesses()
        draw_hang()
        if attempts == 0:
            print(f'You loose. The chosen word was {chosen_word}')
            game_over = True
            
    if "_" not in display:
        game_over = True
        print('You won, You have guessed the word :D') 
