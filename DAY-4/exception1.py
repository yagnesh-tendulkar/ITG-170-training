#Scenario: You ask a user for their age. If they type "twenty" instead of 20, a standard int() conversion will crash the program with a ValueError
#To handle this, you can use a try-except block to catch the exception and provide a user-friendly message instead of crashing the program.
while True:
    try:
        age = int(input("Please enter your age: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")