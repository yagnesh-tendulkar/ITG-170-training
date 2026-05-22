class VowelNotFoundError(Exception):
    pass
def check_vowel(str):
    count=0
    for i in range(len(str)):
        if str[i].lower() in "aeiou":
            count=count+1
    if(count==0):
        raise VowelNotFoundError("no vowels found in the string") 
    else:
        print("number of vowels in string is {}".format(count))       

try:
    check_vowel("cvbops")
except VowelNotFoundError as e:
    print(e.args)
