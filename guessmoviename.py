import random

#Clue 1
print("சாது மிரண்டால் காடு தாங்காது!")

#Answer
answer = ['அசுரன்']

print("Guess the movie name")

guesses = ''

# any number of turns can be used here
turns = 5


while turns > 0:
	
	# counts the number of times a user fails
	failed = 0
	
	# all characters from the input
	# word taking one at a time.
	for char in answer:
		
		# comparing that character with
		# the character in guesses
		if char in guesses:
			print(char)
			
		else:
			print("_")
			
			# for every failure 1 will be
			# incremented in failure
			failed += 1
			

	if failed == 0:
		# user will win the game if failure is 0
		# and 'You Win' will be given as output
		print("You Win")
		
		# this print the correct word
		print("The movie name is: ", answer)
		break

# if user has input the wrong alphabet then
	# it will ask user to enter another alphabet
	guess = input("guess a movie name:")
	
	# every input character will be stored in guesses
	guesses += guess
	
	# check input with the character in word
	if guess not in answer:
		
		turns -= 1
		
		# if the character doesn’t match the word
		# then “Wrong” will be given as output
		print("தவறான பதில்")
		
		# this will print the number of
		# turns left for the user
		print("You have", + turns, 'more guesses')
		
		
		if turns == 0:
			print("சாரி பாஸ்! இன்னைக்கு உங்களால கண்டுபிடிக்க முடியல. சரியான பதில்:", answer)
