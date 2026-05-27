list=[]
n=int(input())
max=0
for i in range(n):
    num=int(input())
    list.append(num)
    if(num>max):
        max=num
print("Largest Number:",max)