def palindrome(string):
    if string == string[::-1]:
        return "Palindrome"
    else:
        return "Not Palindrome"
print(palindrome("madam"))