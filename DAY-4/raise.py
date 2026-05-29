def set(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print(f"Age set to {age}")

try:
    age=int(input("Enter your age: "))
    set(age)
except ValueError as e:
    print(e)