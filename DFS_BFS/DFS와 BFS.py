from collections import deque

N, M, V = map(int, input().split())
tmp = []
for i in range(M):
    a, b = map(int, input().split())
    tmp.append([a, b])

graph = [[] for _ in range(N + 1)]
for x in tmp:
    graph[x[0]].append(x[1])
    graph[x[1]].append(x[0])
for i in graph:
    i.sort()


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, v, visited):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        x = queue.popleft()
        print(x, end=" ")
        for i in graph[x]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


visited = [False] * (N + 1)
dfs(graph, V, visited)
print()
visited = [False] * (N + 1)
bfs(graph, V, visited)
