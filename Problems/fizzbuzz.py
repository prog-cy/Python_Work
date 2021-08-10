#fizzbuzz program for play
while(1):
	num = int(input("Say number= "))
	if(num%3 == 0 and num%5 == 0):
		print(str(num)+" = FizzBuzz")
	else: 
		if(num%3 == 0):
			print(str(num)+" = Fizz")
		else:
			if (num%5 == 0):
				print(str(num)+" = Buzz")
			else:
				print(str(num))
	choice = input("Continue(y/n)")
	if(choice == 'n'):
		break
	
print("Thank you for playing the game")