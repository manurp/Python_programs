from collections import OrderedDict
from re import sub

d = OrderedDict()
for _ in range(int(input())):
    s = input()
    name = sub(r' [0-9]+$', '', s)  # removes any number from the end of the string
    price = int(s.split()[-1])
    d[name] = d.get(name, 0) + price

# print('\n', d)
for key, value in d.items():
    print(key, value)

# from collections import OrderedDict
# D = OrderedDict()
# for _ in range(int(input())):
#     item, space, price = input().rpartition(' ')
#     D[item] = D.get(item, 0) + int(price)
# print(*[" ".join([item, str(price)]) for item, price in D.items()], sep="\n")
