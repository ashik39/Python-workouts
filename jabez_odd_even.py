a=[1,34,45,23,47,56,32,24,13,67,98,90,77,76,3,2]
o=[]
e=[]
for i in range(0,len(a)):
    if (a[i]%2==0):
        e.append(a[i])
    else:
        o.append(a[i])
print("The odd values are",o)
print("The even values are",e)

print("ascending order of numbers: ")
e.sort()
o.sort()
print("EVEN NUMBERS",e)
print("ODD NUMBERS",o)
"""for i in range(0,len(o)-1):
    if o[i]<o[i+1]:
       # print(o[i])
       print("")
    else:
        t=o[i]
        o[i]=o[i+1]
        o[i+1]=t
for i in range(len(o)):
    print(o[i],end=" ")
print("\nascending order of even numbers: ")
for i in range(0,len(e)-1):
    if e[i]<e[i+1]:
       # print(e[i])
       print("")
    else:
        t=e[i]
        e[i]=e[i+1]
        e[i+1]=t
for i in range(len(e)):
    print(e[i],end=" ")
        #print(o[i]) 
#print("The ascending of odd numbers: ",o)"""
























































































