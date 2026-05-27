set=set(map(int,input("Enter numbers:").split()))
max=0
min=0
for x in set:
    if(x>max):
        max=x
    elif(x<min):
        min=x
print("Max:",max)
print("Min:",min)