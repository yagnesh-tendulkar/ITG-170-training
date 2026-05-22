num = int(input("Enter a number: "))
digit_to_find = int(input("Enter digit to count: "))

count = 0

while num > 0:

    digit = num % 10

    if digit == digit_to_find:
        count += 1

    num = num // 10

print("Number of occurrences:", count)