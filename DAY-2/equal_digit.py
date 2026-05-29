#Program to whether all digits in a given number are equal or not.
N=int(input("ENter a integer value:"))
digit = N % 10;

while (N != 0) :
# Find the current last digit
    current_digit = N % 10;

        # Update the value of N
    N = N // 10;

        # If there exists any distinct
        # digit, then return No
if (current_digit != digit) :
    print("No")
else:print( "Yes")