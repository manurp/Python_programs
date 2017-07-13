a = [[input(), float(input())] for i in range(int(input()))]
print(a)
s = sorted(set([x[1] for x in a]))
print(s)
for name in sorted(x[0] for x in a if x[1] == s[1]):
    print (name)