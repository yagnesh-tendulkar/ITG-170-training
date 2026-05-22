number=int(input("enter number of row ."))
for i in range(number):
    for j in range(number-1-i):
        print("*",end="")
    for k in range(i+1):
        print(k+1,end="")
    print()       