# Make immutable string mutable
# Method 1

def add_char(s, pos, c):
    s = s[0:pos]+c+s[pos+1 : ]
    return s

# Defining main function as similar to c language
def Main():
    s = input()
    p, c = input().split()
    print(add_char(s, int(p), c))

# Below written code is checking existance of Main() function
if __name__ == '__main__':
    Main()


