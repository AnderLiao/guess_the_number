# - Create a random number from 1 to 100
# - User can guess a number between the random number
# - Print out "You win" if user guessed the right number
# - Print out "Higher" or "Lower" if the number is wrong
# - Don't stop until the use guess the right one

import random
num_a = int(input('Choose the smallest number: '))
num_b = int(input('Choose the greatest number: '))
roll = random.randint(num_a , num_b)
i = 1
while True:
	print('This is your No. ' + str(i) + ' time(s)')
	user_input = int(input('Guess a number between 1 to 100: '))
	i += 1
	if user_input > roll:
		print('Lower, try again!')
	elif user_input < roll:
		print('Higher, try again!')
	else:
		i -= 1
		print('Bingo! You made it after ' + str(i) + ' time(s)')
		break