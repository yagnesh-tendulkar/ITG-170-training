n = int(input("Enter the last denominator: "))
sum = 0
for i in range(1,n+1):
    sum += 1/(i**2)
print(sum)