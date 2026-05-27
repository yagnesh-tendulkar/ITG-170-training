import pickle

data = {
    "name" : "Rishabh",
    "age"  : 21,
    "company" : "Miracle Software Systems",
    "list" : ["rohan","sohan","mohan"]
  }

with open("FileHandl/data.pkl","wb") as file:
    pickle.dump(data,file)
    
print("Serialized")

with open("FileHandl/data.pkl","rb") as file:
    res=pickle.load(file)
    
print("Deserialized Data")
print(res)