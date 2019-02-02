from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://play2048.co/')
#定位到new game按钮
try:
	linkElem = browser.find_element_by_link_text('New Game')
except:
	print("not found the buttom.")
else:
	linkElem.click()
	print('click pass')
	


htmlElem = browser.find_element_by_tag_name('html')
for i in range(100):
#while True:
	htmlElem.send_keys(Keys.UP)
	htmlElem.send_keys(Keys.RIGHT)
	htmlElem.send_keys(Keys.DOWN)
	htmlElem.send_keys(Keys.LEFT)
	
	try:
		linkElem_gameover = browser.find_element_by_link_text('Try again')
	except:
		pass
	else:
		print("move times=%s"%str(i-1))
		print('scroe', browser.find_element_by_class_name('score-container').text)  #记录页面中的scroe成绩
		linkElem.click()     #游戏失败，重写开始按钮
		#print('click try_again pass')
print('Keys press pass')

