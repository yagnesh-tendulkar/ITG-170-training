print("========================== Check Character ===========================")
def character(ch):
    if ch.isupper():
        print("The character is uppercase")
    elif ch.islower():
        print("The character is lowercase")
    elif ch.isdigit():
        print("The character is digit")
    else:
        print("The character is special character")



ch = input("Enter the single character : ")
character(ch)

