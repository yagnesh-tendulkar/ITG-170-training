for i in range(2,11):
    flag=True
    for j in range(2,i):

        if(i%j==0):
            flag=False
            break
    if(flag):
        print(i)    