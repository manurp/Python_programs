import re

m = re.search('(?<=abc)def', 'abcdef')
m.group(0)
# print(dir(m))
print(m.group(0))

s = 'From-him-to-them: where he: is one of them'
sl = re.findall('^F.+:',s)
print(sl)
sl = re.findall('^F.*:',s)
print(sl)
sl = re.findall('^F.+?:',s)
print(sl)
sl = re.findall('^F.*?:',s)
print(sl)

num = 'He has 52.51 chocolates eats 3 and gives 2'
nl = re.findall('[0-9]+',num)
print(nl)
nl = re.findall('[0-9.]+',num)  #To get floating point numbers
print(nl)
# print(re.search('^H.*3',num))
if re.search('^H.*3',num):
	print('Gotcha')

email = 'From: manoj.r.poojari@gmail.com to xxx'
el = re.findall('\S+@\S+',email)
print(el)
el = re.findall('\S+@\S+?',email)
print(el)
el = re.findall('^From: (\S+@\S+)',email)
print(el)

msg ='He bought a cake of $5.75'
ml = re.findall('\$[0-9.]+',msg)
print(ml[0])