# from collections import deque


# def check_que(q, n):
#     flag = 0
#     for _ in range(n - 1):
#         present = q.pop()
#         next_ = q.pop()
#         q.append(next_)
#         if (present < next_ and flag == 0):
#             flag = 1
#         if(present > next_ and flag == 1):
#             return False
#     return True


# # d = deque()
# for _ in range(int(input())):
#     n = int(input())
#     d = deque(map(int, input().split()))
#     if check_que(d, n):
#         print("Yes")
#     else:
#         print("No")


#https://www.hackerrank.com/challenges/piling-up/problem
for t in range(int(input())):
    l = int(input())
    lst = list(map(int, input().split()))
    # l = len(lst)
    i = 0
    while i < l - 1 and lst[i] >= lst[i + 1]:
        i += 1
    while i < l - 1 and lst[i] <= lst[i + 1]:
        i += 1
    print("Yes" if i == l - 1 else "No")
