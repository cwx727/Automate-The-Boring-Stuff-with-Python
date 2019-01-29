import re

text1 = '    1aA45678    '
text2 = ' Aa-45678ABC A A B- '
text3 = 'Aa3   4567'
text4 = 'a23456   78'
text5 = 'A2345678   '
text6 = 'Aa BbCcD  dEe'
text7 = '    1 aA 45 678 90Bb- '

def strong_password(text,re_text=''):
	if re_text == '':
		strip=re.compile(r'^(\s*)|(\s*)$')
		strip = strip.sub('', text)
		print(strip)
	else:
		strip=re.compile(r'%s'%re_text)
		strip = strip.sub('', text)
		print(strip)
		
strong_password(text1)
strong_password(text2,re_text='A')
strong_password(text3)
strong_password(text4)
strong_password(text5)
strong_password(text6)
strong_password(text7)

