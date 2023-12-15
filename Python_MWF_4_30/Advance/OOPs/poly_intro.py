'''
    Polymorphism :

    "Having many forms"

    >>types :
    1. Overloading :
        method overloading: not possible
        
    2. Overriding:
        method overriding is possible

'''

class Sample:

    def add(self,n1,n2,n3=0,n4=0):
        return n1+n2+n3+n4

s1 = Sample()
print(s1.add(12,3))
print(s1.add(12,3,5))
print(s1.add(12,3,5,7))

print(">>>>in built method overloding")
print(len("hello"))
print(len([12,4,35,4,5]))
print(len((12,34,5,64)))

print("hello"+"world")
print(23+45)


