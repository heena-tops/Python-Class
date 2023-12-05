'''
function parameter types :  

*args : arguments
    single parameterized function can accept mutiple parameter at calling time

**kwargs : keyword arguments
    single parameterized function can accept mutiple parameter
    with key arguments(key value pair) at calling time
'''
print(">>>>>>>>> *args <<<<<<<<<<<<<<<<")
def display(*x):
    print(x)

display(12,34,6.45,"hello",89,34)

print(">>>>>>>>> **kwargs <<<<<<<<<<<<<<<<")
def show(**x):
    print(x)

show(k=12,k3=67,p=093.3)
