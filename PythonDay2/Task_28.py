arr = []
r = int(input("enter range of array: "))
for i in range(1,r+1):
    n = int(input("enter number: "))
    arr.append(n)
visited =[]
for i in arr:
    if i not in visited:
        count =0
        for j in arr:
            if i==j:
                count += 1
        print(f"{i} has occur {count} times")
        visited.append(i)