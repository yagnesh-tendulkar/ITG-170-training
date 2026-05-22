"""From the list below, filter only numbers greater than 5:
[2,5,7,1,9,3,10]
"""
l1=[2,5,7,1,9,3,10]
"""for i in range(0,7):
    if l1[i]>5:
        print(l1[i])"""
greater_than_5=[i for i in l1 if i>5]
print("Number which are greater than 5",greater_than_5)