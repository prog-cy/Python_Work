"""
In this program I am going to make calculator same as real world calculator

"""

def calculator():

	result = 0;

	print("Enter '+' to add")
	print("Enter '-' to subtract")
	print("Enter '*' to multiply")
	print("Enter '/' to divide")
	print("Enter 'q' to exit")

	str = input("= ").split(' ')
	number1 = int(str[0])
	ch = str[1]
	number2 = int(str[2])


	while True:

		if ch == '+':
			result = number1 + number2
		elif ch == '-':
			result = number1 - number2
		elif ch == '*':
			result  = number1 * number2
		elif ch == '/':
			result = number1 // number2

		s = input().split(" ")
		number1 = result
		ch = s[0]
		if ch == 'q':
			print("Ans = ", result)
			break

		number3 = int(s[1])
		number2 = number3


if __name__ == '__main__':
	calculator()		





