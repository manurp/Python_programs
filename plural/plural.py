import re

def plural(noun):
	if re.search('[sxz]$',noun): #Noun ending with s,x or z
		return re.sub('$','es',noun)
	elif re.search('[^aeioudgkprt]h$',noun): #noun ending with h and preceeded by any character that is not in that list of characters
		return re.sub('$','es',noun)
	elif re.search('[^aeiou]y$',noun):
		return re.sub('y$','ies',noun)
	else:
		return noun+'s'

print(plural('kid'))
print(plural('agency'))
print(plural('bass'))
print(plural('rash'))