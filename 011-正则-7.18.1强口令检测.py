import re

text1 = '1aA45678'
text2 = 'Aa-45678'
text3 = 'Aa34567'
text4 = 'a2345678'
text5 = 'A2345678'
text6 = 'AaBbCcDdEe'
text7 = '1aA4567890Bb-'

def strong_password(text):
	pwd_re1 = re.compile(r'\S{8,}').search(text)
	psw_re2 = re.compile(r'[A-Z]+').search(text)
	psw_re3 = re.compile(r'[a-z]+').search(text)
	psw_re4 = re.compile(r'\d+').search(text)
	if pwd_re1 == None or psw_re2 == None or psw_re3 == None or psw_re4 == None:
		print(text + " is not strong password.")
	else:
		print(text + " is strong password.")
		
strong_password(text1)
strong_password(text2)
strong_password(text3)
strong_password(text4)
strong_password(text5)
strong_password(text6)
strong_password(text7)

