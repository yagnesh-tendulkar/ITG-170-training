list1=list(map(int,input("Enter numbers:").split()))
list2=list(map(int,input("Enter numbers:").split()))
for i in list1:
    for j in list2:
        if i==j:
            list2.remove(j)
    list1.remove(i)
print(list1)
print(list2)
