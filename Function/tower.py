
# In this program we have three towers and in first tower we have rings and we have to shift the rings
# from source to destination
# we will use recursive approach to solve this problem

def sd(ndisk, t1, t2, t3):
    if ndisk == 1:
        print('Move disk', ndisk,'from', t1, ' -> ', t3)
        return
    sd(ndisk-1, t1, t3, t2)
    print('Move disk',ndisk,'from', t1, ' -> ', t3)
    sd(ndisk-1, t2, t1, t3)

source = 'A'
temp = 'B'
dest = 'C'

ndisk = int(input("Enter number of disk: "))
sd(ndisk, source, temp, dest)