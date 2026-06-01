arr=[1,2,3,1]
checked=[]
for i in arr:
    if i not in checked:
        count=0
        for j in arr:
            if j==i:
                count+=1
        print(f"{i} occurs {count} times")
        checked.append(i)

