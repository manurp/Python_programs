from itertools import combinations
s,n = input().split()
print(*[''.join(j) for i in range(1,int(n)+1) for j in combinations(sorted(s),i)],sep='\n')