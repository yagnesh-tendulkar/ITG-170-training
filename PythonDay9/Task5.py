lst1 = [1,2,3,4]
lst2 = [5,6,7,8]
lst3 = list(map(lambda x,y : ((x+y),(x-y)), lst1, lst2))
print(lst3)