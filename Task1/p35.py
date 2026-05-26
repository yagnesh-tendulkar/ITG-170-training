n = int(input("Enter the number: "))

temp = n

while temp != 1 and temp>=9:

    total = 0

    while temp > 0:

        dig = temp % 10

        total = total + dig * dig

        temp = temp // 10

    temp = total

if temp == 1:
    print("Happy Number")
else:
    print("Not a Happy Number")