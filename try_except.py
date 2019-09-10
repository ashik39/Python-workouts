try:
    #a = int(inut("Enter A value : "))
    a=c*c
    print("A value is :",a)
except NameError as e:
    print("so, please check whether you defined or not")
except ValueError as s:
     print(s,"\n\nplease enter integer value only")
finally:
    if 10 % 2 == 0:
        print("finally yes")
