# split and join a string using predefined function split() and join(arg)
def split_join(str):
    str = str.split()
    str = '-'.join(str)
    return str

if __name__ == '__main__':
    s = input()
    print(split_join(s))