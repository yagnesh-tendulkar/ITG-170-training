marks = int(input("Enter student marks: "))

if marks >= 35:
    print("Student Passed")

    if marks >= 90:
        print("Rank Obtained: Distinction")
    elif marks >= 75:
        print("Rank Obtained: First Class")
    elif marks >= 60:
        print("Rank Obtained: Second Class")
    else:
        print("Rank Obtained: Pass Class")

else:
    print("Student Failed")
