#Write a program to handle exceptions with Java Throw Keyword. in python raise keyword
try:
    age = int(input("Enter age: "))

    if age < 18:
        raise ValueError("Not eligible for voting")

    print("Eligible for voting")

except ValueError as e:

    if "invalid literal" in str(e):
        print("Enter numeric value only")

    else:
        print(e)