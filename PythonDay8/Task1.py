def check(string):
    up = 0
    lw=0
    for i in string:
        if i.isupper():
            up+=1
        elif i.islower():
            lw+=1
    print("Upper value :",up)
    print("Lower value :",lw)

s = input("Enter a string: ")
check(s)