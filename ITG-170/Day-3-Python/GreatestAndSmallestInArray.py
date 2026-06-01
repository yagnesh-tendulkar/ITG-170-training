arr=[1,2,3,4,5]
big=small=arr[0]
for i in arr:
    if i>big:
        big=i
    if i<small:
        small=i
print(big,small)