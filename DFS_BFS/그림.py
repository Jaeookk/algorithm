import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]


def bfs(x, y, visited):
    q = deque()
    q.append((x, y))
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    cnt = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == 1:
                visited[nx][ny] = True
                q.append((nx, ny))
                cnt += 1
    return cnt + 1


count = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            visited[i][j] = True
            count.append(bfs(i, j, visited))

print(len(count))
if count:
    print(max(count))
else:
    print(0)
