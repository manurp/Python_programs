# #DECORATORS

def decorator_function(outer_function):
	# val=msg

	def wrapper_function(*args,**kwargs):
		print("wrapper_function ran before {}".format(outer_function.__name__))
		return outer_function(*args,**kwargs)
	return wrapper_function

@decorator_function
def display():
	print("Inside the display funct")

display()

@decorator_function
def display_info(name,age):
	print("{} is of age {}".format(name,age))

display_info("Manoj",20)

class decorator_class(object):
	"""docstring for decorator_class"""
	def __init__(self, outer_function):
		self.outer_function=outer_function

	def __call__(self,*args,**kwargs):
		print("inside the call function before {}".format(self.outer_function.__name__))
		self.outer_function(*args,**kwargs)

@decorator_class
def print_info(name,age):
	print("{} is enjoying at the age of {}".format(name,age))

print_info("Bhoomi",17)
# print(help(decorator_class))



from functools import wraps


def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        print("inside log")
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print("inside time")
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result

    return wrapper

import time

@my_logger
@my_timer
def display_info(name, age):
    time.sleep(1)
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('Shamantha', 44)

#Decorator with Arguments

def prefix_func(prefix):
	def decorator_fn(original_function):
		def wrapper_function(*args):
			print(prefix,': Wrapper ran before {}'.format(original_function.__name__))
			original_function(*args)
			print(prefix,': Wrapper ran after {}'.format(original_function.__name__))

		return wrapper_function
	return decorator_fn

@prefix_func('Log')
def say_hi(name1,name2):
	print('{} said hi to {}'.format(name1,name2))

say_hi('Manoj','Bhoomika')