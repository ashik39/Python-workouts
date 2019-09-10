=a=int(input("Enter a value : "))
b=int(input("Enter b value : "))
li=[]
pn=[]
npn=[]
for n in range(a,b+1):
    li.append(n)
for numbers in li:

    isprime = True

    for num in range(2,numbers):
        if numbers% num == 0:
            isprime = False

    if isprime:
        pn.append(numbers)
    else:
        npn.append(numbers)
print("Prime number : ",pn)
print("Non Prime number : ",npn)

s=0
to=[]
for a in pn:
    tot=s+a
    s=tot
to.append(tot)
print("Sum of the prime numbers : ",to)
