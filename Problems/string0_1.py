def swap_case(s):
    s2 = ""
    for i in range(len(s)):
        if s.upper()[i] == s[i]:
            s2 += s.lower()[i]
        elif s.lower()[i] == s[i]:
            s2 += s.upper()[i]
    return s2

if __name__ == "__main__":
    s3 = swap_case(input())
    print(s3)

