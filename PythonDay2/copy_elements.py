print("=========== progarm to copy elements from one array to another ======")
original_arr = list(map(int,input('Enter the values in array : ').split()))
print(original_arr)
copy_arr = [None]*len(original_arr)

def copy_function(original_arr,copy_arr):
    for i in range(len(original_arr)):
        copy_arr[i]=original_arr[i]

    print(f"original array {original_arr}")
    print(f"copy array {copy_arr}")

print(copy_function(original_arr,copy_arr))

