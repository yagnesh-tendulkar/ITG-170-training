print("===============Reverse of the element=======================")

arr=list(map(int,input().split()))
n=len(arr)

for i in range(n-1,-1,-1):
    print(arr[i],end=" ")