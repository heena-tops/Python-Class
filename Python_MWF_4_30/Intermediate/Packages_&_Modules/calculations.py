import mymodule
from MyPackage import logic


n1=int(input("Enter n1 : "))
n2=int(input("Enter n2 : "))

print(mymodule.add(n1,n2))

num=int(input("Enter num to find factorial : "))
print(mymodule.fact(num))

val=int(input("Enter num to find sqrt : "))

print(logic.sqrt(val))
