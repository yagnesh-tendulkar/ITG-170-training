# l=["apple","mango","banana","grapes","oranges"]
# print(l[0])
# print(l[-1])
# Create a list of numbers from 1–10 using list comprehension.
l=[int(val) for i in range(1,11)]
print(l)

# Create a dictionary storing:
d={"Name":"Vaishnavi","age":21,"course":"python"}
print(d["Name"])
print(d["age"])
print(d["course"])



# Create a dictionary comprehension to store squares of numbers from 1–5.
d={x:x**2 for i in range(1,6)}
print(d)



# Create a list of 5 favorite movies and print them using a loop.
d=["a","b","c","d","e"]
for i in d:
    print(i)
# Add a new movie to the list and remove one movie.
d.append("f")
d.remove("c")
print(d)





# Create a dictionary of a product: name, price, quantity
d={"name":"soap","price":150,"quantity":5}
total_cost=d["price"]*d["quantity"]
print(total_cost)


# Use list comprehension to create a list of odd numbers from 1–20.
l=[val for val in range(1,21) if val%2!=0]
print(l)


# From a list of names, filter names longer than 4 letters.
l=["vaishnavi","sravanthi","bhargav","sridevi","raju"]
result=list(filter(lambda x:len(x)>4,l))
print(result)


