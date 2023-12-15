'''
    Exception Handling :

    Concept to handle any abnormal termination of programe


    try : the code which can terminate the programe perhaps
    except : if try will not execute then except will by default
    else: will be execute if try will run properly
    finally: will work as default block

'''

n1=int(input("Enter n1 : "))
n2=int(input("Enter n2 : "))

try:
    c = n1/n2
    print("Div : ",c)

except ZeroDivisionError as n:
    print(n)

except TypeError as t:
    print(t)

else:
    print("Try has been executed")

finally:
    print("default execution every time")
