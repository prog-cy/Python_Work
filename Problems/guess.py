# number guessing game

import random as ra

guess = ra.randint(1, 20)

cnt = 3

while(1):
    num = int(input("Enter a number: "))
    
    if num == guess:
        print("Well played")
        break;
    else:
        print("You have "+str(cnt-1)+" chances")
    
    cnt-=1
    
    if cnt == 0:
        print("You lost the game try next time")
        break;
    

    

