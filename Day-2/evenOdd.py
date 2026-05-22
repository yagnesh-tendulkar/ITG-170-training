num = int(input("Enter a number: "))

even_sum = 0
odd_sum = 0

while num > 0:
    digit = num % 10

    if digit % 2 == 0:
        even_sum += digit
    else:
        odd_sum += digit

    num = num // 10

print("Sum of even digits is:", even_sum)
print("Sum of odd digits is:", odd_sum)
