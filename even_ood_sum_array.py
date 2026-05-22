n=int(input("enter size of the array"))
array=[]
for i in range(n):
    array.append(int(input("enter array elements")))
odd_sum=0
even_sum=0
for i in array:
    if i%2==0 :
        even_sum=even_sum+i
    else :
        odd_sum=odd_sum+i        
print(even_sum,odd_sum)