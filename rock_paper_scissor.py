import random

computer_coice = random.choice(['scissors', 'rock', 'paper'])
user_choice = input('Do you want rock, paper or scissors?\n')

print('Computer choice:', computer_coice)
if computer_coice == user_choice:
    print('TIE')
elif user_choice == 'rock' and computer_coice == 'scissors':
    print('WIN')
elif user_choice == 'paper' and computer_coice == 'rock':
    print('WIN')
elif user_choice == 'scissors' and computer_coice == 'paper':
    print('WIN')
else:
    print('You lose, computer wins :)')