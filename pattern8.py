number=int(input("enter number of rows"))
for i in range(1,number+1):
    for j in range(1,i*2):
        if(j==i):
            print(j,end="")
        else :
            print("*",end="")
    print()            