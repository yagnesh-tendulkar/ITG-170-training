arr=[1,2,3,4,5,2,1]
duplicate=[]

for i in arr:
    count=0
    for j in arr:
        if i==j:
            count+=1
        if count>1 and i not in duplicate:
            duplicate.append(i)
            print(i, end=' ')