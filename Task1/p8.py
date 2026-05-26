n=int(input("Enter the n value "))
for num in range(1,n+1):
    if num>1:
        is_prime=True
        for i in range(2,num):
            if(num%i==0):
                is_prime=False
                break
        if is_prime:
            print(num)