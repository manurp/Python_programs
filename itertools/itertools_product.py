from itertools import product
print(*product([int(a) for a in input().split()], [int(b) for b in input().split()]))

# Different Solutions

# from itertools import product
# print(*product( list(map(int, input().split())), list(map(int,input().split())) ))


# a = list(map(int,input().split()))
# b = list(map(int,input().split()))
# print(' '.join(map(str,product(a,b))))