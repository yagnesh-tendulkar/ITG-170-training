#Compare two numbers entered by the user and print which one is greater.
#Ask the user to enter 2 numbers
two_num = list(map(int,input("Enter 2 numbers:").split()))
#Compare and print greater one
if two_num[0]>two_num[1]:
    print("Greater number",two_num[0])
else:
    print("Greater number",two_num[1])