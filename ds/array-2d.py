# #!/bin/python3

# import os

# Complete the hourglassSum function below.


def hourglassSum(arr):
    max_h_sum = -63  # minimum sum for the given constraint
    for i in range(4):
        for j in range(4):
            h_sum = 0
            for k in range(3):
                h_sum += arr[i][j + k]
            h_sum += arr[i + 1][j + 1]
            for k in range(3):
                h_sum += arr[i + 2][j + k]
            # print(i,j,h_sum)
            if h_sum > max_h_sum:
                max_h_sum = h_sum
    return max_h_sum


arr = []
for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))
result = hourglassSum(arr)
print('Maximum hour glass sum is', result)
# Hackerrank challenge
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     arr = []

#     for _ in range(6):
#         arr.append(list(map(int, input().rstrip().split())))

#     result = hourglassSum(arr)

#     fptr.write(str(result) + '\n')

#     fptr.close()
