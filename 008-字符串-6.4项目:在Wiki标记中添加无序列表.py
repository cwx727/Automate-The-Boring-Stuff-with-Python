#! /usr/bin/python3


import pyperclip
#text = 'Lists of animals\nLists of aquarium life\nLists of biologists by author abbreviation\nLists of cultivars'
text = pyperclip.paste()

lines = text.split('\n')
for i in range(len(lines)):
	lines[i] = '*' + lines[i]
	
text = '\n'.join(lines)	

pyperclip.copy(text)


