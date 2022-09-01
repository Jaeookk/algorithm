from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N + 1)]
for i in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)


def bfs(graph, v, visited):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


answer = 0
visited = [False] * (N + 1)
for i in range(1, N + 1):
    if not visited[i]:
        bfs(graph, i, visited)
        answer += 1

print(answer)
