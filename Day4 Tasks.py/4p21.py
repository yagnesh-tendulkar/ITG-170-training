dict={1:'red', 2:'green', 3:'black', 4:'white', 5:'black'}
l=[]
for k in dict:
    l2=[]
    l2.append(k)
    l2.append(dict[k])
    l.append(l2)
print(l)