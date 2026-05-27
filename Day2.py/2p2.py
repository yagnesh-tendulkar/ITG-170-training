x=int(input("Enter your marks:"))
if(x>=35):
    if(x>=75):
        print("Grade:A")
    elif(x>=50):
        print("Grade:B")
    else:
        print("Grade:C")
    print("You are Passed")
else:
    print("You are Falied")