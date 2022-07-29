from collections import deque
import sys
f = sys.stdin.readline

n, k = map(int, f().split())

graph = []
virus = []
for i in range(n):
    a = list(map(int, f().split()))
    graph.append(a)
    for j in range(n):
        if graph[i][j] != 0:
            virus.append((graph[i][j], 0, i, j)) # 바이러스 종류, 시간, 행, 열

# 시간, 행, 열 위치
s, x, y = map(int, f().split())

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


virus.sort()
queue = deque(virus)

# bfs
while queue:
    v, time, a, b = queue.popleft()
    if time == s:
        break

    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < n and graph[nx][ny] == 0:
            graph[nx][ny] = v
            queue.append((v, time + 1, nx, ny))

print(graph[x - 1][y - 1])   
