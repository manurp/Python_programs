from itertools import permutations
s,n = input().split()
print(*[''.join(i) for i in permutations(sorted(s),int(n))],sep='\n')

#Alternate codes

# from itertools import permutations
# li = input().split()
# strli = list(li[0])
# strli.sort()
# for i in permutations(strli,int(li[1])):
#     for j in i:
#         print(j,end='')
#     print()