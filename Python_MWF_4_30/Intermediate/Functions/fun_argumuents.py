'''
    Types of Fuunction Arguments :

    args : myfun(*args)

    kwargs : myfun(**kwargs)

'''

def add_val(*x):
    total=0
    for k,i in x.items():
        total+=i

    return total


print("Addition of all elements : ",add_val(12,3,5,7))

def add_kw(**x):
    total=0
    for k,i in x.items():
        total+=i

    return total


print("Addition of all elements : ",add_kw(k1=1,k2=9,k3=6))
