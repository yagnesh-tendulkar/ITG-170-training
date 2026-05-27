print("===========find the frequency of each element in the array=============")

arr=list(map(int,input().split()))
dict_={}
for i in arr:
    if i not in dict_:
        dict_[i]=1
    else:
        dict_[i]+=1

for key,val in dict_.items():
    print(f"Item no {key} and frequency {val} ")