numbers = [20, 45, 150, 80]

if any(num > 100 for num in numbers):
    print("List contains a number greater than 100")
else:
    print("No number greater than 100 found")