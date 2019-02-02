import random,logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')


guess = ''
while guess not in (0, 1):
	print('Guess the coin toss! Enter heads or tails:')
	guess = int(input())
	toss = random.randint(0, 1) # 0 is tails, 1 is heads
	if toss == guess:
		print('You got it!')
		logging.info('the 1st time, toss = guess, toss='+str(toss)+', guess='+str(guess))
		break
	else:
		print('Nope! Guess again!')
		logging.info('the 1st time, toss != guess, toss='+str(toss)+', guess='+str(guess))
	guess = int(input())
	if toss == guess:
		print('You got it!')
		logging.info('the 2nd time, toss = guess, toss='+str(toss)+', guess='+str(guess))
		break
	else:
		print('Nope. You are really bad at this game.')
		logging.info('the 2nd time, toss != guess, toss='+str(toss)+', guess='+str(guess))
		break



