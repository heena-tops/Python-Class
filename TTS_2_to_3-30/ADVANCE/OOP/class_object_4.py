class Bird:
    #class member


    #magic method or dunder method

    # __init__ will call automatically when object of such class will createss
    def __init__(self,n1,n2):
        self.num1=n1
        self.num2=n2
    
    def display(self):
        print("num 1 : ",self.num1)
        print("num 2 : ",self.num2)
    

#object creation

o1= Bird(12,3)

o1.display()








