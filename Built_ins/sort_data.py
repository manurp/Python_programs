# https://www.hackerrank.com/challenges/python-sort-sort/problem
# Sorting the rows of the table according to the index of the row given by (k)

n, m = map(int, input().split())  # n is the number of rows in the table and m is the number of colums
# print(n, m)
table = []  # List to store the rows of the table as a list of tuples
for _ in range(n):  # For taking n inputs() from the user which are the rows of the table
    t = tuple(map(int, input().split()))
    table.append(t)

k = int(input())

# print(table)
# print(k)

# Use of merge sort algorithm


def merge(left, right, array):
    i, j, p = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i][k] <= right[j][k]:
            array[p] = left[i]
            i += 1
        else:
            array[p] = right[j]
            j += 1
        p += 1

    while i < len(left):
        array[p] = left[i]
        i += 1
        p += 1

    while j < len(right):
        array[p] = right[j]
        j += 1
        p += 1


def merge_sort(a):
    size = len(a)
    if size < 2:
        return
    if size % 2 == 0:
        mid = size // 2
    else:
        mid = size // 2 + 1
    left = a[0:mid]
    right = a[mid:size]

    merge_sort(left)
    merge_sort(right)
    merge(left, right, a)


merge_sort(table)
for tup in table:
    print(*tup, sep=' ')

# # Elegant solution for the problem
# N, M = map(int, input().split())
# rows = [input() for _ in range(N)]
# K = int(input())
# for row in sorted(rows, key=lambda row: int(row.split()[K])):
#     print(row)
