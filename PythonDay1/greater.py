print("==========Printing greater number by entered by the user===========")
def greater_num(num1,num2):
    if num1>num2:
        print(f"first number {num1} is greater ")
    elif num1==num2:
        print(f"both the numbers {num1}, {num2} are equal .")
    else:
        print(f"second number {num2} is greater .")




num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
greater_num(num1,num2)
