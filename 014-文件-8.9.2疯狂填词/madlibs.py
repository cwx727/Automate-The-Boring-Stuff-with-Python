import re

filename = 'madlibs.txt'
filename_madlabs = 'madlabs_re.txt'

#取出文件中的内容
with open(filename) as f_obj:
	text = f_obj.read()

re_text = text
re_text_groups = re.compile(r'ADJECTIVE|NOUN|VERB|ADVERB').findall(text) #查找文件中的的字符
#print(re_text_groups)

for i in re_text_groups:
	if i[0] == 'A':
		re_text_group = input("Enter an %s:\n" %i.lower())
	else:
		re_text_group = input("Enter a %s:\n" %i.lower())
		
	re_text = re.compile(r'%s' %i).sub(re_text_group, re_text, count=1)  #count=1只替换第一个出现的字符
	
with open(filename_madlabs, 'w') as f_obj:
	f_obj.write(re_text)
		

