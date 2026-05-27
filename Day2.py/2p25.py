for i in range(1,1001):
    sum=0
    s=str(i)
    for j in range(0,len(s)):
        sum+=pow(int(s[j]),len(s))
    if(sum==i):
        print(i)