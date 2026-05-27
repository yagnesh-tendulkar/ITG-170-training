l1=[(10,20,40),(40,50,60),(70,80,90)]
for i in range(0,len(l1)):
    l=list(l1[i])
    l[len(l)-1]=100
    y=tuple(l)
    l1[i]=y
print(l1)
