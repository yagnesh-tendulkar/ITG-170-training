arr=[]
r = int(input("Enter the range of array: "))
for i in range(1,r+1):
    n = int(input("enter number: "))
    arr.append(n)
visited =[]
for i in arr:
    if i not in visited:
        count = 0
        for j in arr:
            if i==j:
                count+=1
        if count>1:
            print("Duplicate elemnts are :",i)
        visited.append(i)