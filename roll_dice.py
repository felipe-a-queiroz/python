import random

roll = random.randint(1,6)

guess = int(input('Guess the dice roll:\n'))

print('The computer rolled a ' + str(roll))
if guess == roll:
    print('Correct!')