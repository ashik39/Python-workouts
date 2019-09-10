class biggest:
    def __init__(self):
        self.a = int(input("Enter the 'a' value: "))
        self.b = int(input("Enter the 'b' value: "))
    def display(self):
        if (self.a > self.b):
            print("the biggest value is 'a' {}".format(self.a))
        else:
            print("The biggest value is 'b' {}".format(self.b))
class reverse(biggest):
    def __init__(self):
        self.c = self.a + self.b
        self.reverse = 0
    def display(self):
        while(self.c > 0):
            self.temp = self.c % 10
            self.reverse = self.reverse * 10 + self.temp
            self.c = self.c // 10
        print("The reversed number is {}".format(self.reverse))
class result(reverse):
    def __init__(self):
        biggest.__init__(self)
        reverse.__init__(self)
    def show(self):
        biggest.display(self)
        reverse.display(self)
obj = result()
obj.show()
    
        
        
    
