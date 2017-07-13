#Generators

def sq_gen(num_list):
	for i in num_list:
		yield i*i

my_list=sq_gen([1,2,3,4,5])
print(my_list)

for num in my_list:
	print(num,end=" ")
print()

mylist = (x**3 for x in [1,2,3,4,5])
print(mylist)

for num in mylist:
	print(num)