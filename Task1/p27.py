n=int(input("Enter the array size : "))
arr=[]
for i in range(n):
    ele=int(input("Enter the array values : "))
    arr.append(ele)
    #arr[i]=int(input("Array value : "))
copy_arr=[0]*n
for i in range(n):
    copy_arr[i]=arr[i]
print("Original arr : ",arr)
print("Copied arr : ",copy_arr)