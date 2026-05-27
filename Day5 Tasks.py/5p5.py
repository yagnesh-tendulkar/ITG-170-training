age = int(input("Enter age: "))
if age < 18:
    raise Exception("Not eligible to vote")
print("Eligible to vote")