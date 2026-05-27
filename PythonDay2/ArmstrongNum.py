print("===========Armstrong Number==================")

def cube(i):
    return i*i*i

def armstrong(num):
    total=0
    temp=num
    while temp>0:
        last=temp%10
        total=total+cube(last)
        temp=temp//10

    if total==num:
        print(f"Armstrong Number is : {num}")




for i in range(1,1000+1):
    if armstrong(i):
        print(i)