print("========= pattern printing ===============")
for i in range(1,8):
    for j in range(6-i,-1,-1):
        print("*",end="")
    for k in range(1,i+1):
        print(k,end="")
    print()