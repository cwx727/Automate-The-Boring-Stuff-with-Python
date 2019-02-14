import time, subprocess

timeLeft = 5
while timeLeft > 0:
	print(timeLeft)
	time.sleep(1)
	timeLeft -= 1

#进程打开文件；#win系统为subprocess.Popen(['start', 'alarm.wav'], shell=True)  
subprocess.Popen(['see', 'alarm.wav'])  
