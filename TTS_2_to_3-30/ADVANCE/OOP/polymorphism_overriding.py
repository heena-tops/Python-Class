'''

Overriding:

having same name & same number of arguments but one method is in parent class
& another is in child class
'''

class Parent:
    def __init__(self):
        print("Hello From Parent")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Hello from Child")


c1 = Child()
