from collections import Counter

input()
shoedict = Counter(map(int, input().split()))
money = 0
for _ in range(int(input())):
    size, amount = map(int, input().split())
    if shoedict[size] > 0:
        money += amount
    shoedict[size] -= 1
print(money)
