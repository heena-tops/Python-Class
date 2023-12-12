class Math:

    def __init__(self,x):
        self.val=x

    #overloading concept throgh method 
    def MyMethod(self,y):
        return self.val+y.val

o1=Math(12)
o2=Math(5)


print(o1.MyMethod(o2))




