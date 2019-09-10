a=[121,131,234]
print("Given list is: ",a)
b=[]
for i in range(len(a)):
    rev=0
    c=a[i]
    while a[i]>0:
        rem=a[i]%10
        rev=(rev*10)+rem
        a[i]//=10
    b.append(rev)
    if c==b[i]:
        print(c,"is palindrome")
    else:
        print(c,"is not a palindrome")
print(b)

