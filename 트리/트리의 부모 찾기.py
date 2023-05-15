# BOJ 11725 실버 2

import sys
from collections import deque


def bfs(graph):
    q = deque([1])
    parent = [0] * 100001  # parent[i] = j -> i의 부모노드가 j

    while q:
        cur = q.popleft()
        for next in graph[cur]:
            # 현재 노드의 부모가 다음 노드라면
            # 즉, 다음 노드가 자식이 아니라 부모노드라면
            if parent[cur] == next:
                continue
            parent[next] = cur
            q.append(next)
    return parent


if __name__ == "__main__":
    input = sys.stdin.readline

    n = int(input())
    graph = [[] for _ in range(n + 1)]
    for i in range(n - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    parent = bfs(graph)

    for i in range(2, n + 1):
        print(parent[i])
