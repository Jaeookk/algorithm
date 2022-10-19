from collections import deque


def bfs(x, y, graph):
    q = deque()
    q.append((x, y))
    graph[x][y] += 1
    while q:
        x, y = q.popleft()
        dx = [1, 1, 2, 2, -1, -1, -2, -2]
        dy = [-2, 2, -1, 1, -2, 2, -1, 1]
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < l and 0 <= ny < l:
                if graph[nx][ny] == -1:
                    q.append((nx, ny))
                    graph[nx][ny] = graph[x][y] + 1


t = int(input())
for _ in range(t):
    l = int(input())
    x, y = map(int, input().split())
    fx, fy = map(int, input().split())
    graph = [[-1 for _ in range(l)] for _ in range(l)]
    bfs(x, y, graph)
    print(graph[fx][fy])
