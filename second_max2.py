n=int(input())
arr=map(int,input().split())
li=list(arr)
maxi=max(li)
for i in range(n):
    if maxi in li:
        li.remove(maxi)
li.sort()
try:
    print(li[-1])
except IndexError:
    print("There is no second number in the list")
