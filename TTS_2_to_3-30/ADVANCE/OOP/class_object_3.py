class Bird:
    #class member


    #magic method or dunder method

    # __init__ will call automatically when object of such class will createss
    def __init__(self):
        self.var=int(input("Enter num : "))
    
    def display(self):
        print(self.var)
    

#object creation

o1= Bird()
o1.display()
