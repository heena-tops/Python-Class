class Sample:

    # class members

    num=89

    #self is default argument for class methods
    # self reprsents current class
    def add(self):
        print("addition : ",self.num+10)
        
    def mul(self):
        print("Mul : ",self.num*10)


# object creation

o1 = Sample()

print("outside of class")
print("Num = ",o1.num)

o1.add()
o1.mul()



