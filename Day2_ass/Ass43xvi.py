"""
******1
*****12
****123
***1234
**12345
*123456
1234567
"""
for i in range(1,8):
    print("*"*(7-i),end="")
    for j in range(1,i+1):        
        print(j,end="")
    print("")