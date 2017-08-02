# Perform append, pop, popleft and appendleft methods on an empty deque d.
from collections import deque

d = deque()
for _ in range(int(input())):
    inp = input().split()
    getattr(d, inp[0])(*[int(inp[1])] if len(inp) > 1 else [])
print(*[item for item in d])
