def n_prime_number(number):
    count=0;
    n=2;
    while(count<number):
        flag=True
        for i in range(2,n):
                
            
                if(n%i==0):
                    flag=False
                    break

        if(flag):
                  count=count+1;
                  print(n)        
        n=n+1
n_prime_number(4)