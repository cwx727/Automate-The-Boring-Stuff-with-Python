def displayInventory(dics):
	#显示玩家的拥有的战利品
	print("Inventory:")
	total_item = 0
	for key, value in dics.items():
		print(str(value) + ' ' + key)
		total_item += value
		
	print("Total number of items: " + str(total_item))
	
def addToInventory(inv, dragonLoot):
	#将征服一条龙的战利品的战利品加入到玩家的战利品字典中
	for temp_dragonLoot in dragonLoot:
		if temp_dragonLoot in inv.keys():
			inv[temp_dragonLoot] += 1   #如果玩家拥有该战利品，字典的战利品value+1
		else:
			 inv[temp_dragonLoot] = 1  #不拥有该战利品，加入字典中，value=1
	return inv
	
	
inv = {'gold coin': 42, 'rope': 1}	#玩家原有的战利品
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']  #征服一条龙的战利品

inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
	

	


	


