from itertools import groupby


print(*[(len(list(c)), int(k)) for k, c in groupby(input())])
# print(*[(list(c), int(k)) for k, c in groupby('1222311')])


# print(groupby('1222311'))

# for i,j in groupby(input()):
# 	print((len(list((j))),int(i)),end=' ')