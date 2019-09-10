a=14466441
s=a
rev=0
print("given value:",a)
while a>0:
    rem=a % 10
    rev=(rev*10)+rem
    a=a//10
print("reverseed value:",rev)
if rev==s:
    print("given value is palindrome")
else:
    print("value is not a palindrome")
