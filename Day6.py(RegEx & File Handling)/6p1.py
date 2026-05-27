def count_case(string):
    upper = 0
    lower = 0

    for ch in string:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1

    print("No. of uppercase characters :", upper)
    print("No. of Lower-case Characters:", lower)

count_case('The quick Brow Fox')