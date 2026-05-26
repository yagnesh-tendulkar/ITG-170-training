num=input("Enter the given number : ")
first_dig=num[0]
temp=True
for i in num:
    if i!=first_dig:
        temp=False
        break
if temp:
    print("All digits are equall")
else:
    print("All the digits are different")