from collections import Counter
d=dict(Counter(list(map(int,input().split()))))
entitiesToRemove = {1,3,4,5}
for x in entitiesToRemove:
    if x in d.keys():
        del d[x]

print(d)
