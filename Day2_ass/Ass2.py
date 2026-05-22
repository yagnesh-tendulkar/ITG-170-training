#Check whether the student passed or failed and if he passed print which rank obtained.
marks = int(input("Enter marks of a student:"))
if (marks>90):
    print("Grade: 'A'")
elif (marks>=80):
    print("Grade: 'B'")
elif (marks>=70):
    print("Grade: 'C'")
elif (marks>=60):
    print("Grade: 'D'")
elif (marks>=50):
    print("Grade: 'E'")
else :
    print("Fail")