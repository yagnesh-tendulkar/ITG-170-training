# #Take a user’s name and print:
# Name in uppercase
# Name in lowercase
# Length of the name

name = input("Enter your name:")
print("Name in uppercase:", name.upper())
print("Name in lowercase:", name.lower())
print("Length of the name:", len(name)) 

#manual reading
upperName=" "
lowerName=""
length=0
for i in name :
    length+=1
    if 'a'<=i<='z':
        upperName+=chr(ord(i)-32)
        lowerName+=i
    elif 'A'<=i<='Z':
        upperName+=i
        lowerName+=chr(ord(i)+32)
    else:
        upperName+=i
        lowerName+=i
print("Name in uppercase:", upperName)
print("Name in lowercase:", lowerName)
print("Length of the name:", length)