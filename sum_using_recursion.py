def sum_num( num):
  if(num==0):
    return 0;
  return (num % 10) + sum_num(num // 10)
result=sum_num(int(input("enter the number")))
print(result)