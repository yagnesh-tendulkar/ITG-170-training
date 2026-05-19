str = input("Enter a string")
lowe = 0
upper = 0
for i in str:
    if i.isupper():
        upper += 1
    elif i.islower():
        lowe += 1
    else:
        pass
print("Upper count",upper)
print("Lower count",lowe)