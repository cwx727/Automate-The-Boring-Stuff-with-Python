import pyautogui, time

#模拟百度点击

searchField = (400, 340)
submitButton = (940, 340)
submitButtonColor = (49, 126, 243)
submitReturn = (128, 160)

formData = [{'text':'Python'},{'text':'Java'}]

pyautogui.PAUSE = 0.5  #等待0.5s

for searchtext in formData:
	print('>>> 5 SECOND PAUSE TO LET USER PRESS CTRL-C <<<')
	time.sleep(15)
	
	# Wait until the form page has loaded.
	'''
	while not pyautogui.pixelMatchesColor(submitButton[0], submitButton[1], submitButtonColor):
		time.sleep(0.5)
		print('wait')
	'''
	print("Entering search text...")
	pyautogui.click(searchField[0], searchField[1])
	
	pyautogui.typewrite(searchtext['text'] + '\t')
	pyautogui.press('enter')
	
	print('Clicked Submit.')
	time.sleep(5)
	
	pyautogui.click(submitReturn[0], submitReturn[1])
	print('Clicked Back.')
	time.sleep(5)
