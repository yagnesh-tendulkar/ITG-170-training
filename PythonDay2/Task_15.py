num = input("Enter a number: ")

sum = 0

for i in range(0, len(num), 2):
    sum += int(num[i])

print("Sum of alternate digits is:", sum)