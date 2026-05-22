"""Ask the user for two numbers and print:
Sum
Difference
Product
Division"""
#Ask the user to enter 2 numbers
two_num=list(map(int,input("Enter 2 numbers:").split()))
#perform arithmetic operations
sum=two_num[0]+two_num[1]
diff=two_num[0]-two_num[1]
product=two_num[0]*two_num[1]
div=two_num[0]/two_num[1]
#print the results
print("Sum:",sum)
print("Difference:",diff)
print("Product:",product)
print("Division:",div)