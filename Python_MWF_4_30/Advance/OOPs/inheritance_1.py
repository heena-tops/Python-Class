class Person:

    def displayP(self):
        print("Hello from Parent")


#inherit Person class to Student Class
class Student(Person):

    def displayS(self):
        print("Hello from Child")

        
s1=Student()
s1.displayS()
s1.displayP()
