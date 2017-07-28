from itertools import combinations

N = int(input())
S = input().split()
K = int(input())

num = 0
den = 0

for c in combinations(S, K):
    den += 1
    num += 'a' in c

print(num / den)


# Bad
# length = int(input()) + 1
# li = input().split()
# k = int(input())
# ind = []
# for i in range(li.count('a')):
#     ind.append(li.index('a', i) + 1)

# num = 0

# for tup in combinations(range(1, length), k):
#     for item in tup:
#         if item in ind:
#             num += 1
#             break

# den = len(list(combinations(range(1, length), k)))

# print(num / den)

# Good
# N = int(input())
# L = input().split()
# K = int(input())

# C = list(combinations(L, K))
# F = filter(lambda c: 'a' in c, C)
# # print(list(F))
# print("{0:.3}".format(len(list(F)) / len(C)))
