##########
# https://www.hackerrank.com/challenges/any-or-all/problem
##########

# Challenge to write in less than 3 lines
n, l = int(input()), list(map(int, input().split()))
print("True" if all(i > 0 for i in l) and any(str(i) == str(i)[::-1] for i in l) else "False")


##Without using all or any
# n = int(input())  # Total n numbers
# num_l = list(map(int, input().split()))  # List of n numbers

# flag = True

# for i in num_l:
#     if i < 0:
#         flag = False

# if flag == True:
#     for i in num_l:
#         if str(i) == str(i)[::-1]:
#             flag = True
#             break
#         flag = False

# print(flag)
