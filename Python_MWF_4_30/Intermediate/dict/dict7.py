d1={'k1':12,'k2':34,'k3':74}


d3={'k4':12,'k2':98,'k5':74}

d1.update(d3) #update the dict

print("updated dict : ",d1)

d1.pop('k2') # will remove element as per key
print(d1)

d1.popitem() # will remove last element byy default
print(d1)

d2={}
d2=d1.copy() # copy one dict to another
print(d2)


d1.clear() # will remove all elements from dict
print(d1)
