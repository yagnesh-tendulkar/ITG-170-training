arr = []
r = int(input("Enter the range: "))
for i in range(1,r+1):
    n = int(input("Enter the number: "))
    arr.append(n)
sum =0
for i in arr:
    sum = sum + i
print("The sum of the elements of the array is = ",sum)