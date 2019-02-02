from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('http://inventwithpython.com')
#定位元素
try:
	elem = browser.find_element_by_class_name("cover-thumb")   #class="card-img-top cover-thumb",class中有空格，取其中一个就行
	print('Found <%s> element with that class name!' %(elem.tag_name))
except:
	print("not found.")
	
	
linkElem = browser.find_element_by_link_text('Read Online for Free')
linkElem.click()
print('click pass')   #点击页面

htmlElem = browser.find_element_by_tag_name('html')
htmlElem.send_keys(Keys.END)
print('Keys.END pass')
htmlElem.send_keys(Keys.HOME)
print('Keys.HOME pass')
