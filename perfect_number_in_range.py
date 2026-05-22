def perfect_number_in_range(start, end):
    for i in range(start,end+1):
        sum=0
        for j in range(1,i):
            if(i%j==0):
                sum=sum+j
        if(sum==i):
          print(i)        
perfect_number_in_range(10,40)          