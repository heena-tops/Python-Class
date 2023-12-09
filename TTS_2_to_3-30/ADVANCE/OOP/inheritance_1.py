'''
    Encapsulation : "Wrapping up of data into a single unit"


    Inheritance : "Ability to adapt behaviour of parent class"

    note :"Object will always created from least child class"

    Types :

    1. single level
    2. Multi level
    3. multiple
    4. heirarchical
    5. Hybrid

'''
class Parent:
    def displayP(self):
        print("Hello from Parent")

class Child(Parent):
    def displayC(self):
        print("Hello from Child")


c1=Child()
c1.displayC()
c1.displayP()












