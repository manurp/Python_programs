names=['Ravi','Shamantha','Manoj','Bhoomika']
ages = [54,44,20,17]

d={}
for n,a in zip(names,ages):
	d[n]=a

print(d)
# print (help(zip))
my_dict = {name:age for name,age in zip(names,ages)}
print(my_dict)

for i in names:
	print(i,":",my_dict[i])