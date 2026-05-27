n=input("Enter n:")
l=len(n)-1
def rev(n,l,num):
    if(l<0):
        return num
    num+=n[l]
    return rev(n,l-1,num)
num=""
print(rev(n,l,num))
