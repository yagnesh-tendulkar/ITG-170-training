def reverse_string(str1,n):
    print("--------------------- REVERSE STRING PROGRAM ----------------------")
    for i in range(n-1,-1,-1):
        print(str1[i])



str1=input("Enter a string : ")
n=len(str1)
print(reverse_string(str1,n))

