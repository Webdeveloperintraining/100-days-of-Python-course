from art import logo
from random import randrange
#Number Guessing Game Objectives:
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

def main():
    print(logo)
    print('Welcome to the number guessing game!')
    number = randrange(1,101)
    print("I'm thinking of a number between 1 and 100.\n")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty.lower() == 'easy':
        attempts = 10
    elif difficulty.lower() == 'hard':
        attempts = 5
    else:
        attempts = 3
        
    game = True
    while game:
        print(f"You have {attempts} remaining to guess the number.")
        player_guess = int(input("Make a guess: "))
        guessing_attempts = guess_number(attempts, player_guess, number)
        if attempts == 0:
            print("You've run out of guesses, you lose.")
            game = False
        elif player_guess == number:
            print(f'You got it! The answer was {number}.')
            game = False
        attempts = guessing_attempts

def guess_number(attempts,guess,number):
    if guess < number:
        print('Too Low')
    elif guess > number:
        print('Too High')
    if guess == number:
        return attempts
    return attempts -1

main()