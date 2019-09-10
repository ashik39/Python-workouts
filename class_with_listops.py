from biggestvalue import Biggest

a = Biggest.display()
print(a)

class Lists:
    def get_values(self):
        self.a=int(input("Enter A value:"))
        self.b=int(input("\nEnter B value:"))
        
    def get_list(self):
        self.list1=[]
        for i in range(self.a,self.b+1):
            self.list1.append(i)

    def factorial(self):
        f=1
        facto=[]
        for j in self.list1:
            fa=f*j
            f=fa
            facto.append(fa)
        print("\n\nFactorial Values of list: ",facto)

    def palindrome(self):
        palindrome=[]
        for j in self.list1:
            rev=0
            c=j
            while j>0:
                rem=j%10
                rev=(rev*10)+rem
                j//=10
            if c==rev:
                palindrome.append(c)
        print("\n\nPalindrome values in the list: ",palindrome)
    def leapyear(self):
        leapyear=[]
        for year in range(len(self.list1)):
            if self.list1[year]%400==0 or self.list1[year]%4==0:
                leapyear.append(self.list1[year])
        print("\n\nLeap years in the list: ",leapyear)

    def odd_even(self):
        odd=[]
        even=[]
        for num in range(len(self.list1)):
            if self.list1[num]%2==0:
                odd.append(self.list1[num])
            else:
                even.append(self.list1[num])
        print("\n\nOdd numbers in the list : ",odd)
        print("Even numbers in the list: ",even)

objo = Lists()
objo.get_values()
objo.get_list()
objo.palindrome()
objo.leapyear()
objo.odd_even()
objo.factorial()
