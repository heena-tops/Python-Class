class Sample:

    def display(self,y,z):
        self.v1=y
        self.v2=z
        print(f'y = {y}, z= {z}')


    def fact(self):
        f=1
        for i in range(1,self.v1+1):
           f*=i
        return f

s1 = Sample()
s1.display(12,4)
print(s1.fact())
