print("=========Program to reverse a number==============")
n1=int(input("Enter a number : "))
nl_s=str(n1)
for i in range(len(nl_s)-1,-1,-1):
    print(nl_s[i],end=" ")