a=[]
re=[]
for i in range(10,20):
    a.append(i)
print("Given values",a)
for i in range(len(a)):
    rev=0
    while a[i]>0:
        rem=a[i]%10
        rev=(rev*10)+rem
        a[i]//=10
    re.append(rev)
print(re)
