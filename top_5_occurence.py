fnmae = input('Enter the file name: ')
if len(fnmae)<1: fnmae = 're1.txt'
fhand = open(fnmae,'r')

count = dict()
for line in fhand:
	line = line.lower()
	words = line.split()
	for word in words:
		count[word] = count.get(word,0) + 1
# print(count)

tmp = list()
for k,v in count.items():
	newt = (v,k)
	tmp.append(newt)

# print('\n',tmp)

tmp = sorted(tmp,reverse=True)

# print('\n',tmp)

for v,k in tmp[:5]:
	print(k,v)

# print(sorted([(v,k) for k,v in count.items()],reverse=True)[:5])