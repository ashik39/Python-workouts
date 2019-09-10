num1=int(input("Enter the initial value: "))
num2=int(input("Enter the last value: "))
print("Given numbers are: ",num1,"and",num2)
sum=0
for i in range(num1,num2+1):
    sum=sum+i
print("Summ of the given range is: ",sum)
