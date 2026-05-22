num = int(input("Enter a number: "))

evensum = 0
oddsum = 0

while num > 0:
    digit = num % 10

    if digit % 2 == 0:
        even_sum += digit
    else:
        odd_sum += digit

    num = num // 10

print("Sum of even digits:", evensum)
print("Sum of odd digits:", oddsum)
