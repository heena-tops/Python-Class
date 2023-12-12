class Math:

    def __init__(self,x):
        self.val=x

    # __add__ method get call when + operator used
    def __add__(self,y):
        return self.val+y.val

o1=Math(12)
o2=Math(5)

o3=o1+o2
print(o3)




