n = int(input("Enter the number: "))
f = 1
sum =0
for i in range(1, n+1):
    f=f*i
    sum += 1/f
print(sum)