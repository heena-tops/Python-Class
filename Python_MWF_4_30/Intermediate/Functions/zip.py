'''
    zip() : zip Function
    
'''
l1=[12,3,45,67,8]
l2=[3,4,6,7,8,67]
l3=[2,4,56,7,8,8]

zip1=zip(l1,l2,l3)

# * : unpack operator

a,b,c=zip(*zip1)

print(a)
print(b)
print(c)
