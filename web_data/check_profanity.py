import urllib.request, urllib.parse, urllib.error

def check_profanity(text):
	connection = urllib.request.urlopen('http://www.wdylike.appspot.com/?q='+text)
	output = connection.read()
	print(output)
	connection.close()

def read_text():
	fhand = open('file.txt')
	contents = fhand.read().split()
	# words = contents.split()
	contents = ''.join(contents)
	contents = contents.rstrip()
	# print(contents,end='')
	check_profanity(contents)
	# for contents in fhand.readlines():
	# 	words = contents.split()
	# 	for word in words:
	# 		check_profanity(word)
	# print(contents)
	fhand.close()
	
read_text()
# check_profanity('shot%in%the%fuck')