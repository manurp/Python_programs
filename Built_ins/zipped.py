n, x = map(int, input().split())
marks_list = [map(float, input().split()) for _ in range(x)]

for tup in zip(*marks_list):
    avg = sum(tup) / x
    print('%.1f' % avg)
