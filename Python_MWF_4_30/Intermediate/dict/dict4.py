# Dicts are iterable

person={
    'id':12009,
    'name':"ABC",
    'email':'abc@gmail.com',
    'address':"Ahmedabad"
    }

person['state']="Gujarat"

# .keys(): return key only
# .values() : return value only
# .items() : return key value pair

for k,v in person.items():

    print(f'{k} : {v}')

