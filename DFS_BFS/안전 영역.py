from collections import deque
import copy

N = int(input())
graph = []
max = 0
for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(N):
        if graph[i][j] > max:
            max = graph[i][j]


def bfs(x, y, height):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] > height and visited[nx][ny] == 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
    return 1


answer = 0
for height in range(max + 1):
    result = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if graph[i][j] > height and visited[i][j] == 0:
                result += bfs(i, j, height)
    if result > answer:
        answer = result
    # answer = max(answer, result)

print(answer)
