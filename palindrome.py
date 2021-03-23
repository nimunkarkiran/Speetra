

def palindrome(str1):
    if len(str1) == 0 or len(str1) == 1:
        return True
    if str1[0] == str1[len(str1)-1]:
        return palindrome(str1[1:len(str1)-1])
    return False

print('dad', palindrome('dad'))
print('abcdcba', palindrome('abcdcba'))
print('pythonfor', palindrome('pythonfor'))