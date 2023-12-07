#dicts are mutable

person={
    'id':12009,
    'name':"ABC",
    'email':'abc@gmail.com',
    'address':"Ahmedabad"
    }

print(person)

person['email']="ahmedabad@gmail.com"
print(person['email'])
print(person.get('email'))
