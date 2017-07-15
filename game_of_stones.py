#https://www.hackerrank.com/challenges/game-of-stones-1/problem
for _ in range(int(input())):
     print(["First","Second"][int(input())%7 in [0,1]])