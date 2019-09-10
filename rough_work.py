a=int(input())
b=[]
for i in range(0,a):
	c=int(input())
	b.append(c)
#print(b)
b.sort() 
#m=min(b)
for j in range(2,0,-1):
	print(b[j])
