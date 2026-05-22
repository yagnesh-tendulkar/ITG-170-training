number=int(input("enter number : "))
for i in range(1,number+1):
    for j in range(i):
        print(i-j,end='')
    print()    