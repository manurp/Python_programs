import logging
import employee

logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('sample.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)
# logger.setLevel(logging.DEBUG)

def add(x,y):
	return x+y
def sub(x,y):
	return x-y
def mult(x,y):
	return x*y
def div(x,y):
	try:
		result = x/y
	except ZeroDivisionError:
		logger.error('Tried to divide by zero\n') #logger.exception() to see full traceback
	else:
		return result

x=10 
y=0
logger.debug('Add: {} + {} = {}'.format(x,y,add(x,y)))
logger.debug('Sub: {} - {} = {}'.format(x,y,sub(x,y)))
logger.debug('Mult: {} * {} = {}'.format(x,y,mult(x,y)))
logger.debug('Div: {} / {} = {}'.format(x,y,div(x,y)))
