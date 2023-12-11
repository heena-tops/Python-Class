import random

print(random.randint(1,100))
print(random.randrange(1,100))

l1=[12,3,45,56,7]
print(random.choice(l1))

random.shuffle(l1)
print(l1)
