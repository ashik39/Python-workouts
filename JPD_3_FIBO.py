u=[1,2,3,4,5,6,7,8,9]
n=len(u)
new=[0,1]
print("Given numbers are: ")
for c in range(n):
    print(u[c],end=" ")
print("\nCount of numbers is :",n)
a=0
b=1
f=0
print("Fibonacci series: ")
#print(a,"\n",b) 
for i in range(2,n):
    temp=a+b
    a=b
    b=temp
    new.append(temp)
    print(new)
p=len(new)
u.sort()
new.sort()

for z in range(p):
    for x in range(p):
        if new[z]==u[x]:
            print(new[z])
        
            
