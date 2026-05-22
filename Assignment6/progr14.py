l=[1,-2,3,4,5]
print(all(i > 0 for i in l ))
print(filter(lambda x: x*x for x in l if x% 2 ==0))