#Closures

import logging
logging.basicConfig(filename="closure.log",level=logging.INFO)

def logger(orig_func):

	def log_msg(*args):
		logging.info('Logger {} ran with arguments {}'.format(orig_func.__name__,args))
		print(orig_func(*args))
	return log_msg

def add(x,y):
	return x+y

def sub(x,y):
	return x-y

add_log = logger(add)
sub_log = logger(sub)

add_log(2,5)
sub_log(2,5)