def fib(max):
	a, b = 0, 1 
	while a < max:
		yield a 
		a, b = b, a + b

fib50 = fib(50)
for i in fib50:
	print(i,end=' ')
print()

def fib(n):
	a, b = 0, 1 
	for i in range(n):
		yield a 
		a, b = b, a + b

fib10 = fib(10)
for i in fib10:
	print(i,end=' ')

print()