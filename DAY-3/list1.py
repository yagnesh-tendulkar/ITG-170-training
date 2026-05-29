# Create a list of 5 fruits and print:
# First fruit
# Last fruit
fruits =["apple","banana","cherry","pineapple","grape"]
print(fruits[0])
print(fruits[-1])


#Create a list of numbers from 1–10 using list comprehension.
numbers = [i for i in range(1,11)]
print(numbers)

#From the list below, filter only numbers greater than 5:
[2,5,7,1,9,3,10]

list2=[2,5,7,1,9,3,10]
result=[i for i in list2 if i>5]
print(result)



#reate a list of 5 favorite movies and print them using a loop.
movies=["bahubali","MCA","RRR","KGF","Dangal"]
res=[i for i in movies]
print(res)
#Add a new movie to the list and remove one movie.
movies.append("KEsAVA")
print(movies)
movies.pop()
print(movies)




print()
#Use list comprehension to create a list of odd numbers from 1–20.
res=[i for i in range(1,21) if i%2!=0]
print(res)


#From a list of names, filter names longer than 4 letters.
names=["John","Alice","Bob","Charlie","Dave"]
res=[i for i in names if len(i)>4]
print(res)