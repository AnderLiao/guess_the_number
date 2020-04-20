# - Create a random number from 1 to 100
# - User can guess a number between the random number
# - Print out "You win" if user guessed the right number
# - Print out "Higher" or "Lower" if the number is wrong
# - Don't stop until the use guess the right one

import random

roll = random.randint(1,100)

while True:
	user_input = int(input('Guess a number between 1 to 100: '))
	if user_input > roll:
		print('Lower, try again!')
	elif user_input < roll:
		print('Higher, try again!')
	else:
		print('Bingo!')
		break