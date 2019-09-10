n=10
a=0
b=1
f=0
print(a)
print(b)
for i in range(2,n+1):
    temp=a+b
    a=b
    b=temp
    print(temp)
    
