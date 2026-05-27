n=int(input("Enter n:"))
cou=0
num=2
while(cou<n):
        fou=0
        for j in range(2,num):
            if(num%j==0):
                fou=1
                break
        if(fou==0):
            print(num,end=" ")
            cou+=1
        num+=1
