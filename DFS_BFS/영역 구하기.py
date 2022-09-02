from sys import *

setrecursionlimit(10**6)

m, n, k = map(int, input().split())

graph = [[0] * n for _ in range(m)]

for i in range(k):
    min_y, min_x, max_y, max_x = map(int, input().split())
    for i in range(min_x, max_x):
        for j in range(min_y, max_y):
            graph[i][j] = 1


def dfs(x, y):
    global width
    if 0 <= x < m and 0 <= y < n and graph[x][y] == 0:
        graph[x][y] = 2
        width += 1
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
    return width


count = 0
result = []
for i in range(m):
    for j in range(n):
        width = 0
        tmp = dfs(i, j)
        if tmp != 0:
            count += 1
            result.append(tmp)
print(count)
result.sort()
print(*result)
