num = int(input("Enter a number: "))
digit = int(input("Enter the digit to count: "))

count = 0
temp = num

while temp > 0:
    rem = temp % 10

    if rem == digit:
        count += 1

    temp = temp // 10

print("Number of occurrences of", digit, "is:", count)
