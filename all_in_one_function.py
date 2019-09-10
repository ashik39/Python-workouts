from datetime import datetime

S= datetime.now()
def all(a,b):

    list1=[]
    for i in range(a,b+1):
        list1.append(i)

    print("\n\nList of the given range: ",list1)

    if a>b:
        print("\n\n",a,"is biggest number in the list")
        big=a
    else:
        print("\n\n",b,"is biggest number in the list")
        big=b
 

    
    f=1
    facto=[]
    for j in list1:
        fa=f*j
        f=fa
        facto.append(fa)
    print("\n\nFactorial Values of list: ",facto)
    
        
    
    
    palindrome=[]
    for j in list1:
        rev=0
        c=j
        
        while j>0:
            rem=j%10
            rev=(rev*10)+rem
            j//=10
        if c==rev:
            palindrome.append(c)
    print("\n\nPalindrome values in the list: ",palindrome)
    
    if a<20:
        
        first=0
        second=1
        fibo=[0,1]
        length=a
        s=0
        for fib in range(2,length):
            s=first+second
            first=second
            second=s
            fibo.append(s)
        print("\n\nFibonnnaci series of A: ",fibo)
    
    
    leapyear=[]
    for year in range(len(list1)):
        
        if list1[year]%400==0 or list1[year]%4==0:
            leapyear.append(list1[year])
    print("\n\nLeap years in the list: ",leapyear)


        

    odd=[]
    even=[]
    for num in range(len(list1)):
        if list1[num]%2==0:
    
            odd.append(list1[num])
        else:
      
            even.append(list1[num])
    print("\n\nOdd numbers in the list : ",odd)
    print("Even numbers in the list: ",even)

    
    
    rever=[]
    
    for re in list1:
        rev=0 
        while re>0:
            rem=re%10
            rev=(rev*10)+rem
            re//=10
        rever.append(rev)
    print("\n\nOriginal values in list: ",list1)
    print("Reversed values in list: ",rever)
    
    prime=[]
    np=[]
    for li in list1:
        if li%2==0 or li%3==0 or li%5==0 or li%7==0:
            np.append(li)
        else:
            prime.append(li)
    print("\n\nNon primme numbers in the list: ",np)
    print("prime numers in the list : ",prime)


    ad=0
    tot=[]
    for s in list1:
        total_sum=ad+s
        ad=total_sum
    tot.append(total_sum)
    print("\n\nSum of all the values in list",tot)


a=int(input("Enter A value:"))
b=int(input("\nEnter B value:"))
all(a,b)               
            

E = datetime.now()

time=E-S
st=str(time)

print("\n\nRunned time in millisecoond: ",st)
