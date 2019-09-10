#a ="sudhagar"

#for i in "ragahdus":
 #   print(i)
    

a=[12,23,45,34]
re=0
for i in a:
   # print(i)
    while i>0:
        r=i%10
        re=(re*10)+r
        i=i//10
        final=re
    print(final)
