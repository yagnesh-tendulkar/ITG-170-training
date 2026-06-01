def isPalindrome(word):
    reverse=word[::-1]
    if(word==reverse):
        return True
    else:
        return False

word= input('Enter a word :')
if(isPalindrome(word)):
    print('Palindrome')
else:
    print('Not Palindrome')