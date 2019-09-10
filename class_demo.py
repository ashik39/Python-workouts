class Demo:
    def get_values(self):
        self.a = 20
        self.b = 30
    def addition(self):
        self.c = self.a + self.b
        print(self.c)

if __name__ == "__main__":
    obj = Demo()
    obj.get_values()
    obj.addition()
    


"""class bird:
    def __init__(self):
        self.hunter = "vultucture"
        self.fly = "High"
    def result(self):
        print("The {} is hunting bird.".format(self.hunter))
        print("This bird is flying very {} ".format(self.fly))
class parrot:
    def __init__(self):
        self.nose = "Red"
        self.food = "Nuts"
    def result2(self):
        print("The parrot nose is {} ".format(self.nose))
        print("The parrot food is {} ".format(self.food))
class birds(bird,parrot):
    def __init__(self):
        bird.__init__(self)
        parrot.__init__(self)
    def result3(self):
        bird.result(self)
        parrot.result2(self)
ob1 = birds()
ob1.result3()"""
