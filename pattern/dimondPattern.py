print("Dimond pattern")
num=5
for i in range(num):
    print(" "*(num-i)+"* "*i)
for i in range(num,0,-1):
    print(" "*(num-i)+"* "*i)