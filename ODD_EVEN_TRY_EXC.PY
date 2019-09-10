def getting():
    value=int(input("\n\nEnter A value : "))
    if value%2==0:
        print("\nGiven value is EVEN")
    else:
        print("\n\nGiven value is ODD")
def get():
    try:
        getting()
    except ValueError as val:
        print("\n\nYou Entered a wrong values")
        print("\nPlease Enter a Numerical Value")
        getting()
#    finally:print("\nProgram executed")
get()
