# 백준 2623 골드3

import sys
from collections import deque


def topology_sort():
    q = deque()
    result = []

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)

        for next in graph[now]:
            indegree[next] -= 1
            if indegree[next] == 0:
                q.append(next)

    return result


if __name__ == "__main__":
    input = sys.stdin.readline

    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)

    for _ in range(m):
        L, *arr = map(int, input().split())
        for i in range(1, L):
            graph[arr[i - 1]].append(arr[i])
            indegree[arr[i]] += 1

    answer = topology_sort()

    if len(answer) != n:
        print(0)
    else:
        for i in range(n):
            print(answer[i])
