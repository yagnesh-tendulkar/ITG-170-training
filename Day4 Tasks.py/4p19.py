d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
res={}
for k1 in d1:
    res[k1]=d1[k1]
for k2 in d2:
    if k2 in res:
            res[k2]=res[k2]+d2[k2]
    else:
            res[k2]=d2[k2]
print(res)