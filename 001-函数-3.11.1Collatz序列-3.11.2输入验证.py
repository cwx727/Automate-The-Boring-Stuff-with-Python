def collatz(number):
	if number%2 == 0:
		return(number//2)
	elif number%2 != 0:
		return(3*number+1)
	elif number == 1:
		return number

try:	
	number = int(input("please input a integer:"))
except ValueError:
	print("it is not a integer")
else:
	print(number)
	while number != 1:
		number = collatz(number)
		print(number)
	

	


	


