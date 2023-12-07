class Person:

    def input(self,name,city):
        self.n=name # class var
        self.c=city # class var

    def info(self):
        print("=====welcome =======")
        print(f'Hello {self.n}, Hope you are doing well in {self.c}')

p1 = Person()
p1.input("ABC","Ahmedabad")
p1.info()

