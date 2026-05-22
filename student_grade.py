marks = int(input("Enter marks: "))

if marks >= 35:

    print("Student Passed")

    if marks >= 90:
        print("Rank: A Grade")
        
    elif marks >= 75:
        print("Rank: B Grade")
        
    elif marks >= 60:
        print("Rank: C Grade")
        
    else:
        print("Rank: D Grade")

else:
    print("Student Failed")