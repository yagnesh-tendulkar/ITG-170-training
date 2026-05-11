num = int(input("Enter a number: "))
digit = int(input("Enter the digit to find: "))

count = 0

while num > 0:
    rem = num % 10

    if rem == digit:
        count += 1

    num = num // 10

print("Number of occurrences:", count)