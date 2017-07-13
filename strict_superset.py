def strict_superset(a):
    for i in range(int(input())):
        b=set(input().split())
        if not(a-b!=set() and b-a==set()):
            return False
    return True
print(strict_superset(set(input().split())))