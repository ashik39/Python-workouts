a=[1,2,3,4,5,6,7,8,9]
count=0
for i in a:
    for j in range(len(a)):
        if a[j]%i==0:
            count+=1
        
