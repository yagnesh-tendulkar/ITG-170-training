row=int(input("enter number of rows ."))
for i in range(1,row+1):
    for j in range(1,i+1):
        if(j==1):
            print(j,end="")
        else:
            print("*{}".format(j),end="")
    print()            