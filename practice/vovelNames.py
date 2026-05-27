names = ["Anil", "Bob", "Isha", "Ravi", "Uma"]

vov_names=list(filter(lambda x:x[0].lower() in "aeiou" ,names ))
print(vov_names)