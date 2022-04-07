import random
count = 0

while True:
	r = random.randint(1,1000)
	count = count + 1
	if r != 9:
		print(r)
		continue
	elif r == 9:
		print(r)
		print('Got a 9 with', count, 'counts')
		break 