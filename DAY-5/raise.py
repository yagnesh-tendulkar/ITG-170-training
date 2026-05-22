try:
    age = int(input("Enter your age: "))

    if age < 18:
        raise Exception("You are not eligible to vote")

    print("You are eligible to vote")

except Exception as e:
    print("Error:", e)