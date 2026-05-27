n=int(input("Enter n : "))
sum_series = 0

for i in range(1,n+1):
    sum_series+=1/(i**2)

print("Sum :",sum_series)