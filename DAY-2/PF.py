marks = int(input())

if marks < 35:
    print("Fail")
else:
    print("Pass")
    if marks >= 90:
        print("1st Rank")
    elif marks >= 80:
        print("2nd Rank")
    elif marks >= 70:
        print("3rd Rank")
    else:
        print("Pass Class")
