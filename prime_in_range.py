def prime_in_range(start,end):
    for i in range(start,end+1):
        if i<2:
           continue
        flag=True
        for j in range(2,i):
         if(i%j==0):
          flag=False
          break
        if(flag):
           print(i)
prime_in_range(1,10)           