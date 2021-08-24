# count total number of substring in a original string

def count_number(s1, s2):
    s1 = "".join(s1)
    s2 = "".join(s2)
    count = 0
    for i in range(len(s1)):
        if s1[i:len(s2)+i] == s2:
            count+=1
    return count

def Main():
    s1 = input().split()
    s2 = input().split()
    n = count_number(s1, s2)
    print(n)

if __name__ == '__main__':
    Main()
