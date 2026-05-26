num=input("Enter the number ")
sum=0
for i in range (0,len(num),2):
    sum=sum+int(num[i])
print(sum)