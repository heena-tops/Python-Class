# list tuple as dict element
import random

person={
    'id':12009,
    'name':"ABC",
    'email':'abc@gmail.com',
    'address':"Ahmedabad",
    'Hobby':['Cricket','Football','Hocky','Rugby']
    }


print("using index : ",person['Hobby'][2])

print("random :")
element=random.choice(person['Hobby'])
print(element)

for i in person.values():
    print(i)
