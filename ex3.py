try:
    print("Outer try block")

    try:
        num1 = int(input("Enter first : "))
        num2 = int(input("Enter second number: "))

        result = num1 / num2
        print("Result =", result)

    except ZeroDivisionError:
        print("Inner Exception: Cannot divide by zero.")

    except ValueError:
        print("Inner Exception: Invalid input.")

except Exception as e:
    print("Outer Exception:", e)

finally:
    print("Program ended.")