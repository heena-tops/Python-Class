class A:
    def __init__(self):
        self.n1=90   #public 
        self._n2=32  #protected
        self.__n3=87 #private

    def display(self):
        print(self.n1)
        print(self._n2)
        print(self.__n3)


a1 = A()

#Name Mangling : access private members of class
print(a1._A__n3)
