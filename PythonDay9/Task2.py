list= [1,2,2,3,3,4,5,5]
u=[]
for i in list:
    if i not in u:
        u.append(i)
print(u)