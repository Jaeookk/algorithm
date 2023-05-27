# 백준 2252 골드3

import sys
from collections import deque


def topology_sort():
    result = []
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        node = q.popleft()
        result.append(node)

        for next in graph[node]:
            indegree[next] -= 1
            if indegree[next] == 0:
                q.append(next)

    return result


if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1

    print(*topology_sort())
