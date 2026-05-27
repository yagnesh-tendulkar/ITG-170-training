n=input("Enter n:")
ans=0
def sum(n,l,ans):
    if(l<0):
        return ans
    ans+=int(n[l])
    return sum(n,l-1,ans)
l=len(n)-1
print(sum(n,l,ans))