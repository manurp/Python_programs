def add(x,y):
	return x+y
def sub(x,y):
	return x-y
def mult(x,y):
	return x*y
def div(x,y):
	if (y==0):
		return "Zero division Error!!"
	return x/y
import logging
logging.basicConfig(filename='calculations.log',level=logging.INFO,format='%(asctime)s:%(levelname)s:%(message)s')
x=10 
y=15
logging.info('{} + {} = {}'.format(x,y,add(x,y)))
logging.info('{} - {} = {}'.format(x,y,sub(x,y)))
logging.info('{} * {} = {}'.format(x,y,mult(x,y)))
logging.info('{} / {} = {}'.format(x,y,div(x,y)))
