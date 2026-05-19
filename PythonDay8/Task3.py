def isPalindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False
s= "Madam"
print(isPalindrome(s))