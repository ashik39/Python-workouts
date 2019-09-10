u=[]
l=len(u)

n=30
new=[0,1]
#print("\nCount of numbers is :",n)
a=0
b=1
f=0
#print("Fibonacci series: ")
#print(a,"\n",b) 
for i in range(2,n):
    temp=a+b
    a=b
    b=temp
    new.append(temp)
#print(new)
p=len(new)
u.sort()
new.sort()
print("fibo numbers are: ")
for z in range(p):
    for x in range(l):
        if u[x]==new[z]:
            print(new[z])
        
            
