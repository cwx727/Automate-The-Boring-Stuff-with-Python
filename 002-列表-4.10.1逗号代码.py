def list_transfer_string(lists):
	string = ''
	for temp_list in lists[:-1]:
		string = string + temp_list + ', '
	string += 'and '+lists[-1]
	return(string)
	
spam = ['apples', 'bananas', 'tofu', 'cats']
print(list_transfer_string(spam))
	

	


	


