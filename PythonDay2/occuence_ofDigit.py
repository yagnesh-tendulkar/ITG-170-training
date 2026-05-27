print("Program to print the occurence of digit in a number")

def occ_digit(num, digit):
    count=0
    for i in num:
        if i==digit:
            count+=1
    print(f"the digit {digit} occured {count} times in the number")       




num=input("Enter a number : ")
digit = input("Enter the digit to find occurence")
occ_digit(num,digit)