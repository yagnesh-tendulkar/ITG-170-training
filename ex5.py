try:
    age = int(input("Enter your age: "))

    if age < 18:
        raise ValueError("Age must be 18 or above.")

    print("You are eligible.")

except ValueError as e:
    print("Exception occurred:", e)

finally:
    print("Program completed.")