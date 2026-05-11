num = input("Enter a number: ")

flag = True

for i in range(len(num) - 1):
    if num[i] != num[i + 1]:
        flag = False
        break

if flag:
    print("All digits are equal")
else:
    print("Digits are not equal")