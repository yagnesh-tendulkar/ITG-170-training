try:
    name = (input("Enter your name: "))
    print("Hlo! ", name)

except ValueError:
    print("Invalid input.")

finally:
    print("finally block executed")