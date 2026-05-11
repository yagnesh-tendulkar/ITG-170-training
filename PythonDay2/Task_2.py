marks = int(input("Total marks scored by the student: "))#Maximum marks = 500
if marks>=200:
    if (marks>=480) and (marks<=500):
        print("Student has passed with a grade of A")
    elif (marks>=400) and (marks<480):
        print("Student has passed with a grade of B")
    elif (marks>=300) and (marks<400):
        print("Student has passed with a grade of C")
    elif (marks>=200) and (marks<300):
        print("Student has passed with a grade of D")
else:
    print("Student has Failed")
