class Bird:

    # method as class member
    def fly(self):
        print("Duck can Fly")

class Animal:

    def run(self):
        print("Cheeta can run fast")


#object creation
b1= Bird()
a1=Animal()

b1.fly()
a1.run()

print(type(b1))
print(isinstance(b1,Bird))
print(isinstance(a1,Animal))
