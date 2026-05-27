arr = list(map(str,input("Enter movies into list : ").split()))
for i in arr:
    print(i,end=" ")

arr.append(input("enter a  movie: "))
print(arr)
arr.remove(input("Remove a movie: "))
print(arr)