from itertools import combinations_with_replacement

s,n = input().split()
print(*[''.join(j) for j in combinations_with_replacement(sorted(s),int(n))],sep='\n')

#Alternatively
# for i in combinations_with_replacement(sorted(s),int(n)):
# 	print(''.join(i))

