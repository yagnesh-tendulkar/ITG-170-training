#From a list of names, filter names longer than 4 letters.
names=["Hari","Sampat","Harini","Harinita","Dhanush","Hani"]
"""for i in names:
    if len(i)>4:
        print("Long name:",i)"""
long_names=[i for i in names if len(i)>4]
print("Long names:",long_names)