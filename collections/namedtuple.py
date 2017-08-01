# n = int(input())
# li = input().split()
# s = 0
# for _ in range(n):
#     s += int(input().split()[li.index('MARKS')])
# print(s / n)

# Challenge to solve in less than 4 lines
# n, mark_index = int(input()), input().split().index('MARKS')
# print(sum([int(input().split()[mark_index]) for _ in range(n)]) / n)

# Using namedtuple
from collections import namedtuple
n, Student = int(input()), namedtuple('Student', input())
print(sum([float(stud.MARKS) for stud in [Student(*input().split()) for _ in range(n)]]) / n)
# li = [Student(*input().split()) for _ in range(n)]
# print(li)
