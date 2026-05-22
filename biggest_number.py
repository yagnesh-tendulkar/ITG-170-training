num = int(input("Enter a number: "))

big = 0

while num > 0:
    digit = num % 10

    if digit > big:
        big = digit

    num = num // 10

print("Biggest digit is:", big)