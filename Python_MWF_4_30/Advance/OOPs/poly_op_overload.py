class A:
    def __init__(self,n1):
        self.num=n1

    def __add__(self,y):
        return self.num+y.num


a1=A(12)
a2=A(5)


print(a1+a2)
