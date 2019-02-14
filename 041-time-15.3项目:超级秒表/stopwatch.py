import time

print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch.Press Ctrl-C to quit.')
input()
print('Started.')
startTime = time.time()
lastTime = startTime
lapNum = 1

try:
	while True:
		input()
		lapTime = round(time.time() - lastTime, 2) #2代表取小数点后2位
		totalTime = round(time.time() - startTime, 2)
		print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')	
		lapNum += 1
		lastTime = time.time()
except KeyboardInterrupt:
	print('\nDone')
