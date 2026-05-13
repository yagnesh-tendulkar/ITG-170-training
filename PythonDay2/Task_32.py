arr = []
r = int(input("Enter the range: "))
for i in range(1,r+1):
    n = int(input("Enter the elements: "))
    arr.append(n)
while len(arr)>0:
    largest = arr[0]
    for i in arr:
        if i > largest:
            largest = i
    print(largest,end = " ")
    arr.remove(largest)