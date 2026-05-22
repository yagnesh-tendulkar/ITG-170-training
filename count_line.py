with open('example.txt','r') as file:
    count=0
    for i in file:
        count=count+1
print(count)