rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
from random import randint
print(' ')

human = int(input('What do you choose? Type 0 for ROCK, 1 for PAPER, 2 for SCISSORS: '))
while human not in range(0,3):
    print('Wrong input! Please try again')
    human = int(input('What do you choose? Type 0 for ROCK, 1 for PAPER, 2 for SCISSORS: '))

choices = [rock, paper, scissors]

print('\nYou chose: \n' + choices[human])

computer = randint(0,2)
print('\nComputer chose: \n' + choices[computer])

if computer == 0 and human == 1:
    print("\nYou Win!")
elif computer == 1 and human == 0:
    print("\nYou Loose!")

elif computer == 2 and human == 1:
    print("\nYou Loose!")
elif computer == 1 and human == 2:
    print("\nYou Win!")

elif computer == 0 and human == 2:
    print("\nYou Loose!")
elif computer == 2 and human == 0:
    print("\nYou Win!")

elif computer == human :
    print("\nIt's a draw!")