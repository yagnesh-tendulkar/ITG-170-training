print("------------------------:big digit in a number :---------------")
number =input("Enter a number : ")
big_digit=0
for i in number:
    if int(i)>big_digit:
        big_digit = int(i)

print("The big digit is : ",big_digit)