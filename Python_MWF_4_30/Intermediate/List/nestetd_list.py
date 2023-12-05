# Nested Lists

l1 = [23,5,[2,55,90,[4],99],92,34,65]

print(l1[2][3][0])
print(l1[-4][-2][-1])

print("Length of List : ",len(l1))


print(">>>>>>>>>>>>>>>>>>>task Solution : ")
# task :  create list with Distinct elements only

l2=[12,34,56,76,87,12,34,43,76,56]
unique_list=[]

for element in l2:
    if element not in unique_list:
        unique_list.append(element)

print("unique list : ",unique_list)
