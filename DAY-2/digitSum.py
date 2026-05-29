#Program to print the sum of alternative digits in a given number.
phone=input("Enter your phone number:")
even=0
odd=0
for i in phone[0::2]:
    even+=(int(i))
for i in phone[1::2]:
    odd+=(int(i))
totalSum=even+odd
print(f"alternativedigit Sum is :{totalSum}")