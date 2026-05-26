sq={x:x**2 for x in range(10) if x%2==0}
print(sq)
key=['a','b','c']
value=[1,4,8]
dic={k:v for k,v in zip(key,value)}
print(dic)