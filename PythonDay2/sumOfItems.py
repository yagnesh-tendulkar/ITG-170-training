print("=======================: Sum of all items in an array :========================")

sum_ofItems=0
arr=list(map(int,input("Enter an array : ").split()))
for i in range(len(arr)):
    sum_ofItems+=arr[i]

print("The sum of all items are : ",sum_ofItems)