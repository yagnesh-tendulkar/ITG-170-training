num= input('Enter a number: ')
def compareDigits(num):
    for i in num:
        for j in num:
            if i!=j:
                return False
    return True
print(compareDigits(num))