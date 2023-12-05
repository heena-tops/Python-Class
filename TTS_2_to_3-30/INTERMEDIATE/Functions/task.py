# print 10 to 1 using recursion

def reverse(x):
    if x>=0:
        print(x)
        return reverse(x-1)
    else:
        return 0
        
num=int(input("Enter num : "))
reverse(num)
