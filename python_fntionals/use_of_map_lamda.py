def cube(x): return x**3
# If lamda is used
# cube = lambda x:x**3

def fibonacci(n):
    first_num = 0
    next_num = 1
    fib_list = []
    if n < 1:
        return []
    if n < 2:
        return [0]
    if n < 3:
        return [0, 1]

    for i in range(0, n):
        fib_list.append(first_num)
        temp = next_num
        next_num += first_num
        first_num = temp
    return fib_list


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
