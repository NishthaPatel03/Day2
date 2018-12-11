#Check whether given string is palindrome or not using recursion.

def palindrome(string):
    if(len(string)==0 or len(string)==1):
        return True
    else:
        if (string[0]==string[-1] and palindrome(string[1:-1])):
            return True
        else:
            return False

str1='Nishtha'
str2='abcba'
print(str1,'is palindrome:',palindrome(str1))
print(str2,'is palindrome:',palindrome(str2))