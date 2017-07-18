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

street = '100 NORTH BROAD ROAD'
print(re.sub('ROAD$','RD.',street)) #Replaces the sub-string ROAD by RD. from a string which ends with ROAD 
street = '100 NORTH BROAD'
print(re.sub('ROAD$','RD.',street))
street = '100 NORTH BROAD'
print(re.sub('\bROAD$','RD.',street))  #\b, which means “a word boundary must occur right here."
street = '100 BROAD ROAD APT. 3'
print(re.sub('\bROAD\b','RD.',street)) 
print(re.sub(r'\bROAD\b','RD.',street)) #r is raw_string tells nothing in the string sholud be escaped

print()
#Roman Numbers
#checking for thousands
pattern = '^M?M?M?$'  #Zero to three matches in a row '$'- no other characters after M
print(re.search(pattern,'MMM'))
pattern = '^M{0,3}$'  #Alternative to previous pattern
print(re.search(pattern,'MMMM'))
print(re.search(pattern,''))
print()
#Checking for hundreds

pattern = '^M?M?M?(CM|CD|D?C?C?C?)$' # 'a|b' used to match either of a and b
print(re.search(pattern,'MCM'))
# MCM' matches because the first M matches, the second and third M characters are ignored, and the CM
# matches (so the CD and D?C?C?C? patterns are never even considered). MCM is the Roman numeral
# representation of 1900.
print(re.search(pattern,'MD'))
print(re.search(pattern,'MMMCCC'))
print(re.search(pattern,'MCMC'))
print(re.search(pattern,''))
print()
#Try to find All roman characters

pattern = '^M?M?M?(CM|CD|D?C?C?C?)(L?X?X?X?|XC|XL)(IX|IV|V?I?I?I?)$'
print(re.search(pattern,'MCCCXLVI')) #1346
print(re.search(pattern,'MCCCXXVI')) #1326
pattern = '^M{0,3}(CM|CD|D?C{0,3})(L?X{0,3}|XC|XL)(IX|IV|V?I{0,3})$'
print(re.search(pattern,'MDLV')) #1555
print(re.search(pattern,'MCCCXXXIV')) #1334
print(re.search(pattern,'MCCCXXXIIV'))
print(re.search(pattern,'MMMDCCCLXXXVIII')) #3888 Longest...

#VERBOSE All white spaces are ignored and contents after #
pattern = '''
^ 					# beginning of string
M{0,3} 				# thousands - 0 to 3 Ms
(CM|CD|D?C{0,3}) 	# hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 Cs),
					# or 500-800 (D, followed by 0 to 3 Cs)
(XC|XL|L?X{0,3}) 	# tens - 90 (XC), 40 (XL), 0-30 (0 to 3 Xs),
					# or 50-80 (L, followed by 0 to 3 Xs)
(IX|IV|V?I{0,3}) 	# ones - 9 (IX), 4 (IV), 0-3 (0 to 3 Is),
					# or 5-8 (V, followed by 0 to 3 Is)
$ 					# end of string
'''

print(re.search(pattern,'MCDIV',re.VERBOSE)) #re.VERBOSE is necessary which is a constant
print(re.search(pattern,'MCDIV'))   #Assumes as compact regular expression when not specified as verbose
