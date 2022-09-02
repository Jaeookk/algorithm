from collections import deque

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(graph, v, visited):
    count = 0
    q = deque()
    q.append(v)
    visited[v] = True
    while q:
        x = q.popleft()
        next_arr = graph[x]
        for next in next_arr:
            if not visited[next]:
                q.append(next)
                visited[next] = True
                count += 1
    return count


visited = [False] * (N + 1)
print(bfs(graph, 1, visited))
