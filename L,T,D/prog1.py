# Write a program to print the sum of elements in a List
# def L_sum(lists):
#     return sum(lists)
# lists = [1,2,3,4]
# print(L_sum(lists))
# Write a program to get the Largest Number in the List.
# def lar(Lists):
#     return max(Lists)
# Lists = [1,2,3,4]
# print(lar(Lists))
# Remove Common Elements from two Lists
l1 =[1,2,3,4]
l2 = [5,4,3,2]
if len(l1) <= len(l2):
    k = len(l2)
else:
    k = len(l1)

for i in range(0,k):
    if l1[i] == l2[i]:
        l1.remove(l1[i])
        l2.remove(l2[i])
print(l1,l2)

