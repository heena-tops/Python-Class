'''
task: 

l1=[12,3.434,45,"Hello",74,34.54,"Happy",'alpha']

o/p:
strs=["Hello","Happy",'alpha']
ints=[12,45,74]
floats=[3.434,34.54]

'''
l1=[12,3.434,45,"Hello",74,34.54,"Happy",'alpha']

strs=[]
ints=[]
floats=[]

for element in l1:
    if isinstance(element,int):
        ints.appen(element)

'''
import random

l1=[12,3.434,45,"Hello",74,34.54,"Happy",'alpha']

print(random.choice(l1))'''

