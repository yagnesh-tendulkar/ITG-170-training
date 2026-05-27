list1=[6, 5, 3, 9]
list2=[0, 1, 7, 7]

list3=list(map(lambda x,y:[x+y,x-y] ,list1,list2))
print(list3)