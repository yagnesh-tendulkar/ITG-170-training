for num in range(1, 1001):

    temp = num
    sum = 0
    digit=0
    while(temp!=0):
        digit=digit+1
        temp=temp//10
    
    temp=num
    while temp != 0:

        rem = temp % 10
        sum = sum + (rem ** digit)
        temp = temp // 10

    if sum == num:
        print(num)