import art, game_data, random

def main():
    score = 0
    data_length = len(game_data.data)
    end_game = False

    while end_game != True:
        print(art.logo)

        option_a = define_options(data_length)
        option_b = define_options(data_length)
        while option_a == option_b:
            option_a = define_options(data_length)
            option_b = define_options(data_length)

        print(f'Compare A: {option_a['name']}, {option_a['description']}, from {option_a['country']}.')
        print(art.vs)
        print(f'Compare B: {option_b['name']}, {option_b['description']}, from {option_b['country']}.')
        
        user_choice = input("Who has more followers? type 'A' or 'B': ")

        if user_choice.lower() == 'a':
            guess = option_a['follower_count']
            alternative = option_b['follower_count']
        elif user_choice.lower() == 'b':
            guess = option_b['follower_count']
            alternative = option_a['follower_count']
        else:
            print("\nPlease try again, write a valid option.".upper())
            continue

        if guess > alternative:
            score+=1
            print(f"\nYou're right! Current score: {score}.")
        elif guess == alternative:
            print("They have the same amount of followers !!!")
        else:
            end_game = True

    print(f"\nSorry, that's wrong. Final score: {score}")

def define_options(data_length):
    option = game_data.data[random.randrange(data_length)]
    return option

main()