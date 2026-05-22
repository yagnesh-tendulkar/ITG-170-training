num = int(input("Enter a number: "))

sum_alt = 0
position = 0

while num > 0:
    digit = num % 10

    if position % 2 == 0:
        sum_alt += digit

    num = num // 10
    position += 1

print("Sum of alternate digits is:", sum_alt)
