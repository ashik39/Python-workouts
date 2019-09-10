print("\n**Username should be characters\n\n**Password should be numbers")
def verify():
    print("SIGN UP")
    u=str(input("User name : "))
    p=int(input("\nPassword : "))
    print("SIGN IN")
    username=str(input("\nUser name : "))
    paw=int(input("Password : "))
    if username==u and paw==p :
        print("\nYour successfully logged in :)")
    else:
        print("\nNOT SIGNED IN \n*You Entered wrong datas")

def validation():
    try:
     """print("SIGN UP")
        u=str(input("User name : "))
        p=int(input("\nPassword : "))
        print("SIGN IN")
        username=str(input("\nUser name : "))
        paw=int(input("Password : "))""""
        verify()
    except ValueError as V:
        print("Error is: ",V,"\n\nPlease check the datas Entered :(")
        verify()
validation()
