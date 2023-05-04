import sys
from collections import deque


def bfs(v):
    queue = deque([v])
    visited = [-1] * (n + 1)
    visited[v] = 0
    while queue:
        cur = queue.popleft()

        for next in graph[cur]:
            if visited[next] == -1:
                visited[next] = visited[cur] + 1
                queue.append(next)
    return visited


if __name__ == "__main__":
    input = sys.stdin.readline

    n, m = map(int, input().split())  # n : 헛간의 개수, m : 간선의 개수
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    result = bfs(1)
    k = max(result)
    print(result.index(k), k, result.count(k))
