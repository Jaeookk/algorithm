from collections import deque
import sys

m, n, h = map(int, sys.stdin.readline().split())

graph = []
for i in range(h):
    graph.append([list(map(int, sys.stdin.readline().split())) for _ in range(n)])
# print(graph)
# print(graph[0][0][1])


def bfs(graph, time=0):
    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]
    q = deque()
    for i in range(n):
        for j in range(m):
            for k in range(h):
                if graph[k][i][j] == 1:
                    q.append((i, j, k, 0))
    while q:
        x, y, z, time = q.popleft()
        for k in range(6):
            nx = x + dx[k]
            ny = y + dy[k]
            nz = z + dz[k]
            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h and graph[nz][nx][ny] == 0:
                graph[nz][nx][ny] = 1
                q.append((nx, ny, nz, time + 1))
    return time


flag = True
result = bfs(graph)
for i in range(n):
    for j in range(m):
        for k in range(h):
            if graph[k][i][j] == 0:
                flag = False

if not flag:
    print(-1)
else:
    print(result)
