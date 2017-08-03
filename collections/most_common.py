# https://www.hackerrank.com/challenges/most-commons/problem
from collections import Counter

sd = Counter(sorted(input()))

for key in sorted(sd, key=sd.get, reverse=True)[:3]:
    print(key, sd[key])


#
# from collections import Counter, OrderedDict


# class OrderedCounter(Counter, OrderedDict):
#     pass


# [print(*c) for c in OrderedCounter(sorted(input())).most_common(3)]


#
# from collections import Counter
# from operator import itemgetter

# for item in (sorted(sorted(Counter(input()).items()), key=itemgetter(1), reverse=True)[:3]):
#     print(item[0], item[1])


#
# from collections import Counter

# for letter, counts in sorted(Counter(input()).most_common(),key = lambda x:(-x[1], x[0]))[:3]:
#     print (letter, counts)
