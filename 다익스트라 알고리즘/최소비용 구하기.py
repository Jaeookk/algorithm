# 백준 1916 골드5

import sys
import heapq


def dijkstra(start, end):
    q = []
    heapq.heappush(q, (0, start))

    INF = int(1e9)
    distance = [INF] * (n + 1)
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue

        for next in graph[now]:
            cost = dist + next[1]
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(q, (cost, next[0]))

    return distance[end]


if __name__ == "__main__":
    input = sys.stdin.readline

    n = int(input())
    m = int(input())

    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))

    start, end = map(int, input().split())

    print(dijkstra(start, end))
