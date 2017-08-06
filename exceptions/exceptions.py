# https: // www.hackerrank.com / challenges / exceptions / problem
# for _ in range(int(input())):  # Number of test cases
#     try:
#         a, b = map(int, input().split())
#         print(a // b)
#     except ZeroDivisionError as e:
#         print("Error Code:", e)
#     except ValueError as e:
#         print("Error Code:", e)

for i in range(int(input())):
    a, b = input().split()
    try:
        print(int(a) // int(b))
    except (ZeroDivisionError, ValueError) as e:
        print("Error Code:{}".format(e))
