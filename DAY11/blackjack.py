import art, random
print(art.logo)
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def main():
    game = True
    while game:
        game = input("Do you want to play a game of BlackJack?' (Type 'y' or 'n'): ")
        if game.lower() == 'n':
            game = False
            break
        
        your_cards = get_starting_cards()
        player_score = sum(your_cards)
        print(f'Your cards: {your_cards}, current score: {player_score}')
        
        computer_cards = get_starting_cards()
        computer_score = sum(computer_cards)
        print(f'Computer\'s first card: {computer_cards[0]}')

        get_new_card = ''
        while get_new_card.lower() != 'n':
            if computer_score >= 21 or player_score >= 21:
                find_winner(computer_cards,your_cards)
                break

            while computer_score <= 17:
                computer_cards = new_card(computer_cards)
                computer_score = sum(computer_cards)

            get_new_card = input("Type 'y' to get another card, type 'n' to pass: ")
            
            if get_new_card.lower() == 'y':
                your_cards = new_card(your_cards)
                player_score = sum(your_cards)
                print(f'Your cards: {your_cards}, current score: {player_score}')
                print(f'Computer\'s first card: {computer_cards[0]}')
        else:
            find_winner(computer_cards,your_cards)

def get_starting_cards():
    """Adds two cards everytime is called"""
    selected_cards = []
    for _ in range(2):
        selected_cards.append(random.choice(cards))
    if 11 in selected_cards and sum(selected_cards) > 21:
        ace(selected_cards)
    return selected_cards

def new_card(deck):
    deck.append(random.choice(cards))
    if 11 in deck and sum(deck) > 21:
        ace(deck)
    return deck

def ace(deck):
    '''This function identifies the ace card and changes its value if score is greater than 21'''
    while 11 in deck and sum(deck) > 21:
        index = deck.index(11)
        deck[index] = 1
    return deck
            
def find_winner(computer_cards, your_cards):
    '''This functions compares the computer score with the player score and declares who wins'''
    total_computer = (sum(computer_cards))
    total_player = (sum(your_cards))

    print(f'\nYour final hand: {your_cards}, final score: {total_player}')
    print(f'Computer\'s hand: {computer_cards}, final score: {total_computer}')

    if total_computer == 21 or (total_computer > total_player and total_computer < 21):
        print('You loose\n')
    elif total_player == 21 or (total_player > total_computer and total_player < 21):
        print('You win\n')
    elif total_player > 21 and total_computer > 21:
        print('Everyone bust, nobody won!\n')
    elif total_player > 21:
        print('You bust, the computer wins\n')
    elif total_computer > 21:
        print('The computer busts, you win\n')
    else:
        print('It\'s a tie\n')

main()