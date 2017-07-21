class Fib:
	'''iterator that yields numbers in the Fibonacci sequence'''
	def __init__(self,max):
	    self.max=max

	def __iter__(self):
	    self.a=0
	    self.b=1
	    return self

	def __next__(self):
	    fib=self.a
	    if fib>self.max:
	        raise StopIteration
	    self.a,self.b=self.b,self.a+self.b
	    return fib
fib1 = Fib(1000)
for n in fib1:
	print(n,end=' ')
print()
for n in Fib(100):
	print(n,end=' ')
print()
print(fib1)
print(fib1.__class__)
print(fib1.__doc__)