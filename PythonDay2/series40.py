n=int(input("Enter a Number: "))
sum_series = 0
fact=1

for i in range(1,n+1):
    fact*=i
    sum_series+=1/fact


print("Sum is :",sum_series)