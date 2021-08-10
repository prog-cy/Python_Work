#Game to guess the jumbling word
import random as rand

def choose():
	words = ['boat', 'rainbow', 'dog', 'lion','pizza', 'village','bear', 'gang', 'dictionary','dear', 'door', 'dumb','during','doodle','root']
	pick = rand.choice(words)
	return pick

def jumble(word):
	jumb = "".join(rand.sample(word, len(word)))
	return jumb

def thank(p1n, p2n, p1, p2):
	print(p1n, " your score is ", p1)
	print(p2n, " your score is ", p2)
	if(p1 == p2):
		print("Game Draw ")
	elif(p1>p2):
		print("Winner is ", p1n)
	else:
		print("Winner is ", p2n)
	print("Thank you for playing")

def play():
	p1name = input("Enter your name ")
	p2name = input("Enter your name ")
	p1s = 0
	p2s = 0
	turn = 0
	while(1):
		#computer task
		picked_word = choose()
		
		#jumbling the word
		qn = jumble(picked_word)
		print(qn)
		
		#player 1 task
		if(turn%2 == 0):
			print("Your turn ", p1name)
			ans = input("Enter word ")
			if(ans == picked_word):
				p1s = p1s+1
			else:
				print("Better luck, try next time")
				print("picked word is ", picked_word)
			choice = int(input("Enter 1 to continue 0 to exit"))
			if(choice == 0):
				thank(p1name, p2name, p1s, p2s)
				break
		#player 2 task
		else:
			print("Your turn ", p2name)
			ans = input("Enter word ")
			if(ans == picked_word):
				p2s = p2s+1
			else:
				print("Better luck, try next time")
				print("picked word is ", picked_word)
			choice = int(input("Enter 1 to continue 0 to exit"))
			if(choice == 0):
				thank(p1name, p2name, p1s, p2s)
				break
		turn = turn+1
				
play()