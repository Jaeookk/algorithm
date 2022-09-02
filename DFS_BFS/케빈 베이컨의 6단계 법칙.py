import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(graph, start):
    count = [0] * (n + 1)
    visited = [start]
    queue = deque()
    queue.append(start)

    while queue:
        a = queue.popleft()
        for i in graph[a]:
            if i not in visited:
                count[i] = count[a] + 1
                visited.append(i)
                queue.append(i)
    return sum(count)


result = [
    1e9,
]
for i in range(1, n + 1):
    result.append(bfs(graph, i))

print(result.index(min(result)))
