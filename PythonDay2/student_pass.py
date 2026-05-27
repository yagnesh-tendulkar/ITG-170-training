print("====================student pass or fail===================")
marks = int(input("enter marks: "))
if marks >= 91 and marks <= 100:
    print("Student passed with A grade")
elif marks >= 81 and marks < 90:
    print("Student passed with B grade")
elif marks >= 71 and marks < 80:
    print("Student passed with C grade")
elif marks >= 61 and marks < 70:
    print("Student passed with D grade")
elif marks >= 51 and marks < 60:
    print("Student passed with E grade")
elif marks >= 40 and marks < 50:
    print("Student passed with E+ grade")
else :
    print("Student Failed with F grade")