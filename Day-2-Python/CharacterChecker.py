word=input('Enter a word: ')
if word.islower():
    print('Lowercase')
elif word.isupper():
    print('Uppercase')
elif word.isnumeric():
    print('Number')
else:
    print('Special Character')
