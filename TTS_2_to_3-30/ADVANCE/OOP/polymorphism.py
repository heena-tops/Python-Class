'''

    Polymorphism : "Having many forms"

    >>Types :

        1. Overloading:
            - method overloading
                is not possible in python
        2. Overridding
            having same name & same
                number of arguments but
                one method is in parent class
                & another is in child class
'''

class Sample:

    def add(self,a,b):
        return a+b

    def add(self,x,y,z):
        return x+y+z

    def add(self,p,q,r,s):
        return p+q+r+s


s1 = Sample()

print(s1.add(3,4,5,2))











    
