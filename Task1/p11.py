n=int(input("Enter the number "))
total=0
for i in range(1,n):
    if(n%i==0):
        total=total+i
if n==total:
    print("This is an perfect number ")
else:
    print("This is not an perfect number ")