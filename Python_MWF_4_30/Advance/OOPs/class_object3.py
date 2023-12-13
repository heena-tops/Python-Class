# dunder/magic method in python
class Sample:

    # __init__() : call automatically when object of class is created
    def __init__(self,x,y):
        self.n1=x
        self.n2=y

    def display(self):
        print(f'x = {self.n1}, y = {self.n2}')

    # __str__(): call automatically & return string when object is created
    def __str__(self):
        return "Hello"


s1=Sample(12,4)
print(s1)
s1.display()
