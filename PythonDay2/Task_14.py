def sum(num):
    if num ==0:
        return 0
    return(num % 10)+sum(num // 10)
num = int(input("Enter a number: "))
print("Sum of digits is:", sum(num))
