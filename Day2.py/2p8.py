for i in range(2,11):
    fou=0
    for j in range(2,int(i/2) + 1):
        if(i%j==0):
            fou=1
            break
    if(fou==0):
        print(i)
    else:
        continue
