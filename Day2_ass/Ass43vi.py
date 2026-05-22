"""
1
23
456
78910
1112131415"""
num=1
for i in range(1,6):
    for j in range(1,i+1):
        print(num,end=" ")
        num+=1
    print("")