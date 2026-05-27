user_num1 = int(input("Enter a first number: "))
user_num2 = int(input("Enter second number: "))
if user_num1 > user_num2:
    print(f"The first number {user_num1} is greater than the second number {user_num2}")
elif user_num1 < user_num2:
    print(f"The second number {user_num2} is greater than the first number {user_num1}")
else:
    print("Both the number are same")