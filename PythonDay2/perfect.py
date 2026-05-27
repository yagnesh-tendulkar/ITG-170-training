print("========:Perfect number logic:========")

def perfect_number(n):
    if n<=0:
        return False
    
    count=0
    for i in range(1,n):
        if n%i==0:
            count+=i

    if count==n:
        print("It's a perfect number")
    else:
        print("not a perfect number")


n=int(input("Enter Number ; "))
print(perfect_number(n))