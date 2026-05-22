def dupliacte_items(arr):
    duplicate=[]
    for i in range(len(arr)):
        count=0
        if arr[i] in duplicate:
            continue
        for j in range(i,len(arr)):
            if(arr[i]==arr[j]):
                count=count+1
        if(count>1):
            duplicate.append(arr[i])        
    return duplicate;
print(dupliacte_items([10,20,10,30,40,20])    )       