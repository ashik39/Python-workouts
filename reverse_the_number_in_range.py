a =[]
b = []
for i in range(10,20):
    a.append(i)
for j in a:
    rev=0
    while j>0:
        t=j%10
        rev=(rev*10) + t
        j//=10
    b.append(rev)
print("original_list: ",a)
print("reverse_value: ",b)
