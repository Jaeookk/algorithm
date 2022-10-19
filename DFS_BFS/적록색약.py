from collections import deque


n = int(input())
graph = [list(input()) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    temp = graph[x][y]
    visited[x][y] = True
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and graph[nx][ny] == temp:
                    q.append((nx, ny))
                    visited[nx][ny] = True


for k in range(2):
    count = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i, j)
                count += 1
    print(count, end=" ")
    if k == 1:
        break
    visited = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] == "G":
                graph[i][j] = "R"
