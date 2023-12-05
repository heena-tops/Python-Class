'''
Recursive Function :

A function that call itself again and again is called as recursive function


eg:

# fact(5) = 5*fact(4)
# fact(4) = 4*fact(3)
# fact(3) = 3*fact(2)
# fact(2) = 2*fact(1)
# fact(1) = 1*1

'''

def fact(x):
    if x==0:
        return 1
    else:
        return x*fact(x-1)

num=int(input("Enter number to Find Factorial : "))


print("Factorial is : ",fact(num))



















