#implementing dictionary and sets
#creating a dictionary
d={"name":"puspanjali",
   "age":21,
   "course":"python"}
print(d)
#accessing values
print(d["name"])
print(d["age"])
print(d["course"])
#adding items to a dictionary
d["gender"]="female"
d["role"]="it"
print(d)
#updating existing value
d["name"]="anjali"
d["age"]=20
print(d)
#deleting items from a dictionary
d.pop("gender")
print(d)
#iterating over dictionary elements
for i in d:
    print(i)
for i in d.values():
    print(i)
for i,j in d.items():
    print(i,j)
    


