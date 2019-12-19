if __name__ == '__main__':
    s = input()
    i=0
    alpha=False
    alnum=False
    digit=False
    lower=False
    upper=False
    for i in range(len(s)):
        if s[i].isalnum():
            print("True")
            alnum=True
            break
    if i==len(s)-1 and alnum==False:
        print("False")
    for i in range(len(s)):
        if s[i].isalpha():
            print("True")
            alpha=True
            break
    if i==len(s)-1 and alpha==False:
        print("False")
    for i in range(len(s)):
        if s[i].isdigit():
            print("True")
            digit=True
            break
    if i==len(s)-1 and digit==False:
        print("False")
    for i in range(len(s)):
        if s[i].islower():
            print("True")
            lower=True
            break
    if i==len(s)-1 and lower==False :
        print("False")
    for i in range(len(s)):
        if s[i].isupper():
            print("True")
            upper=True
            break
    if i==len(s)-1 and upper==False:
        print("False")
