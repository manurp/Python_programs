from collections import OrderedDict

d = OrderedDict()
for _ in range(int(input())):
    word = input().rstrip()
    d[word] = d.get(word, 0) + 1

print(len(d))
print(*d.values())

# Elegant solution
# https://www.hackerrank.com/external_redirect?to=https://codefisher.org/catch/blog/2015/06/16/how-create-ordered-counter-class-python/
# from collections import Counter, OrderedDict


# class OrderedCounter(Counter, OrderedDict):
#     pass


# d = OrderedCounter(input() for _ in range(int(input())))
# # print(d)
# print(len(d))
# print(*d.values())
