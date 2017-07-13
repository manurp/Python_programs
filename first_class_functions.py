#First Class Functions

def square(x):
	return x*x

def cube(x):
	return x*x*x

def  my_map(func,arg_list):
	result=[]
	def inner_func():
		for i in arg_list:
			result.append(func(i))
		print(result)
	return inner_func

f = square
print(square)
print(f(5))
fun = my_map(square,[1,2,3,4,5])
# print(fun())
fun()
cube_fn = my_map(cube,[1,2,3,4,5])
cube_fn()
print()

def logger():
	def log_message(msg):
		print('Log: {}!'.format(msg))
	return log_message

log = logger()
log("Hi")
log("Hello")

def html_tag(tag):
	def wrap_text(msg):
		print('<{}>{}</{}>'.format(tag,msg,tag))
	return wrap_text

tagh1 = html_tag('h1')
tagp = html_tag('p')
print()
tagh1('This is the heading')
tagp("This is the paragraph")