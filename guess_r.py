import random
start = input('Please select the start number: ')
end = input('Please select the end number: ')
start = int(start)
end = int(end)
r = random.randint(start,end)
count = 0

while True:
	guess = input('Guess a number: ')
	guess = int(guess)
	count = count + 1

	print('This is your', count, 'guesses')
	if guess == r:
		print('You get the right answer!')
		break
	elif guess != r:
		if guess > r:
			print('The number must be smaller')
		elif guess < r:
			print('The number must be bigger')

