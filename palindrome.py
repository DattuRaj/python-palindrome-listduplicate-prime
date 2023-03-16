s=input('enter a string to check palindrome')
s1=""
for i in range(len(s)):
    s1+=s[len(s)-i-1]

print(s1)
if s==s1:
    print('strings is palindrome')
else:
    print('not palindrome')
    