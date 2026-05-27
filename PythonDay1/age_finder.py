from datetime import date

def find_age(dob):
    today = date.today()
    age = today.year - dob.year
    has_passed = (today.month,today.day) < (dob.month,dob.day)

    return age - has_passed

dob=date(2005,3,26)
print(f" Age : {find_age(dob)} years")