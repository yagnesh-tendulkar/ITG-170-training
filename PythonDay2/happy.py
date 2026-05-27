def is_happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        for i in str(n):
            n=sum(int(i)**2)
    
    return n == 1

number = 19
if is_happy(number):
    print(f"{number} is a Happy Number!")
else:
    print(f"{number} is not a Happy Number.")