#Funciton Creation
def myFunction():

    #global variable 
    global name
    name="XYZ"
    #name is local variable
    name1=input("Enter Name : ")
    return name1


# funciton calling
print("Return value from Funciton : ",myFunction())


print("global var : ",name)
