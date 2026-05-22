#file handling and exception handling

filename = "sample.txt"

try:
    with open(filename, "w") as file:
        file.write("Python File Handling Example\n")
        file.write("Learning exceptions too!")

    with open(filename, "r") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("File not found")

except PermissionError:
    print("Permission denied")

except Exception as e:
    print("Something went wrong:", e)

finally:
    print("Execution completed")
