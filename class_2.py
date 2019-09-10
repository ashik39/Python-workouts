class Do:
    def get(self):
        self.a=10
        self.b=20
    def add(self):
        self.c=self.a+self.b
        print(self.c)
obj = Do()
obj.get()
obj.add()
