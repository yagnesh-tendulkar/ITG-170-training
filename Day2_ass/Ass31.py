#Program to find Largest Number and smallest in an Array.
arr=[1,2,3,5,4,9,6,8,7]
largest=arr[0]
smallest=arr[0]
for i in arr:
    if i> largest:
        largest=i
    if i< smallest:
        smallest=i
print("Enter the largest number:",largest)
print("Enter the smallest number:",smallest)