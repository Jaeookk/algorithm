from collections import deque


f, s, g, u, d = map(int, input().split())
graph = [-1] * (f + 2)


def bfs(k):
    global graph
    q = deque()
    q.append(k)
    graph[k] = 0
    dx = [u, -d]
    while q:
        x = q.popleft()
        for i in range(2):
            nx = x + dx[i]
            if 1 <= nx <= f and graph[nx] == -1:
                q.append(nx)
                graph[nx] = graph[x] + 1


bfs(s)
if graph[g] == -1:
    print("use the stairs")
else:
    print(graph[g])
