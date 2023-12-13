class Sample:

    def input(self,x,y):
        self.n1=x
        self.n2=y

    def display(self):
        print(f'x = {self.n1}, y = {self.n2}')


class Bird:

    def bird_types(self,t1,t2):
        self.t1=t1
        self.t2=t2

    def display(self):
        print("Type 1 : ",self.t1)
        print("Type 2 : ",self.t2)

s1=Sample()
s1.input(23,5)
s1.display()

b1=Bird()
b1.bird_types("udi_sake","na_udi_sake")
b1.display()
