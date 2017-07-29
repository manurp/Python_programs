import itertools


k, m = map(int, input().split())
arrays = [map(int, input().split()[1:]) for _ in range(k)]
# k = 3
# m = 1000
# arrays = [[5, 4], [7, 8, 9], [5, 7, 8, 9, 10]]

def f(*nums):
    return sum(x * x for x in nums) % m

# print(list(itertools.product(*arrays)))
# print(arrays)
# print(list(itertools.starmap(f, itertools.product(*arrays))))
print(max(itertools.starmap(f, itertools.product(*arrays))))


# from itertools import combinations


# def f(x):
#     return x * x


# def max_it(a):
#     for j in set(combinations(li, k)):
#         yield sum([f(a[x][y]) for x, y in zip(range(len(a)), j) if y < len(a[x])]) % m


# def max_len(a):  # yields the length of the dictionary value lists
#     for key in a.keys():
#         yield len(a[key])
# # a = {0: [2, 4, 5], 1: [8, 9, 3, 7], 2: [8, 9, 10, 5, 7]}
# # l = [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4]


# k, m = map(int, input().split())
# # print(k, m)
# a = {}
# for i in range(k):
#     a[i] = list(set(map(int, input().split()[1:])))

# li = []
# max_lenOfList = max(max_len(a))
# # print(max_lenOfList)
# for i in range(k):
#     li += range(max_lenOfList)

# # print(l)
# res = max_it(a)
# print(max(res))
