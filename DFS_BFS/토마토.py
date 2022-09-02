from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]


def bfs(graph, time=0):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q = deque()
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                q.append((i, j, 0))
    while q:
        x, y, time = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 0:
                graph[nx][ny] = 1
                q.append((nx, ny, time + 1))
    return time


result = bfs(graph)
for arr in graph:
    if 0 in arr:
        print(-1)
        break
else:
    print(result)
