import re
a = input()
b = input()
match = re.findall('(?='+b+')',a)
print (len(match))
