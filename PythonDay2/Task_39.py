n = int(input("Enter the last power: "))
sum = 0
for i in range(0,n+1):
    sum += 1/(2**i)
print(sum)