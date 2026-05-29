#Ask the user to enter their birth year and calculate their age.
birthYear=int(input("Enter your birth year:"))
currentYear =2026

age=currentYear - birthYear
print("Your age is :", age)
print(f"Your age is : {age}")
print("Your age is : %d" % age)