n = int(input("Enter number: "))
def is_happy(num):
    visited = set()
    while num != 1 and num not in visited:
        visited.add(num)
        s = 0
        while num > 0:
            digit = num % 10
            s += digit * digit
            num //= 10
        num = s
    return num == 1
if is_happy(n):
    print("Happy Number")
else:
    print("Not a Happy Number")