def is_palindrome(s):
    return s == s[::-1]
str= input("Enter a string: ")
print(is_palindrome(str))