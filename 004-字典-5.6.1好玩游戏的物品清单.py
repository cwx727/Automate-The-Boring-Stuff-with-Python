def displayInventory(dics):
	print("Inventory:")
	total_item = 0
	for key, value in dics.items():
		print(str(value) + ' ' + key)
		total_item += value
		
	print("Total number of items: " + str(total_item))
	
	
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

displayInventory(stuff)
	

	


	


