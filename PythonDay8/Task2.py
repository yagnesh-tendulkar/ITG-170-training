def short(lst):
    lst2=[]
    for i in lst:
        if i not in lst2:
            lst2.append(i)
    return lst2

s= [1,2,2,2,3,3,4,5,5]
print(short(s))