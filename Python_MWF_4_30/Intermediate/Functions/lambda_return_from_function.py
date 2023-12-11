# lambda funciton return from another Function

def val(x):

    return lambda y : x*y


n=val(12)

print(n(2))
