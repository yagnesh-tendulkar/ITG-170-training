array=[10,20,30,40,10,20,30,40]
visited=[]
for i in range(len(array)):
    if array[i] in visited:
        continue
    count=0
    for j in range(len(array)):
        if(array[i]==array[j]):
            count=count+1;
    visited.append(array[i])       
    print("{}frequency  is {}".format(array[i],count))
    print(visited)


    