A = set(input().split());
print (all(map(lambda x: (A > x), [set(input().split()) for i in range(int(input()))]))) 