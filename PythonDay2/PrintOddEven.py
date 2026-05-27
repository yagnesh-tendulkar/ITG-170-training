print("=================Odd and Even Numbers from an Array===================")

arr=list(map(int,input("Enter a array here : ").split()))
evenList = []
oddList = []
for i in range(len(arr)):
    if arr[i]%2==0:
        evenList.append(arr[i])
    else:
        oddList.append(arr[i])

print("The even number from the list : ",evenList)
print("The odd number from the list : ",oddList)