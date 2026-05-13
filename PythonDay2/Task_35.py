n = int(input("Enter the number: "))

while n != 1 and n != 4:

    sum = 0

    while n > 0:
        r = n % 10
        sum = sum + (r * r)
        n = n // 10

    n = sum

if n == 1:
    print("This is a happy number")
else:
    print("This is not a happy number")