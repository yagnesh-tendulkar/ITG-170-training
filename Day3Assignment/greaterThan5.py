list1=[2,5,7,1,9,3,10]

# for i in range(len(list1)):
#     if list1[i]>5:
#         print(list1[i])


result =list(filter(lambda x:x>5,list1))
print(result)

