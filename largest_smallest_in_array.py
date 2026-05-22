array=[10,200,30,40,40,50,1,909]
gre=array[0]
low=array[0]
for i in range(len(array)):
    if(gre<array[i]):
        gre=array[i]
    if(low>array[i]):
        low=array[i]
print(gre,low)            