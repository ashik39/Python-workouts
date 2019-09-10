a=int(input("A:"))
b=int(input("B:"))

big = {i:"even" if i%2==0 else "odd" for i in range(a,b)}

print(big)
