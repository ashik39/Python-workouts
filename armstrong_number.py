a=int(input("Enter the value: "))
t=a
print("length of number: ")
ar=0
for i in range(1,a+2):
    s=a%10
    c=s*s*s# change "s" here according to number of digits :)
    ar=c+ar
    a=a//10
if t==ar:
    print("its an armstrong number")
else:
    print("its not an armstrong number")
