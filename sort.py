list=[10,2,3,5,6,4,7,89]
list.sort(reverse=True)
print(list)
#sort using manual
def sort_ascending(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if(arr[i]>arr[j]):
                arr[i],arr[j]=arr[j],arr[i]
    return arr;
print(sort_ascending(list))