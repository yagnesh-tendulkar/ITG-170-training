'''write a Python function that accepts a string and counts the number of
upper and lowercase letters. Sample String: 'The quick Brow Fox'
Expected Output: No. of uppercase characters : 3'''
string = input("Enter a sentence:")
def count_upper(string):
    count = 0
    for char in string:
        if char.isupper():
            count += 1
    print("No of upper case letters are: ", count)
def count_lower(string):
    count=0
    for char in string:
        if char.islower():
            count += 1
    print("No of lower case letters are: ", count)

count_lower(string)
count_upper(string)
