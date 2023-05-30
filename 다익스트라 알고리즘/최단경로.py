# 백준 1753 골드4

import sys
import heapq


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
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


if __name__ == "__main__":
    input = sys.stdin.readline

    INF = int(1e9)
    v, e = map(int, input().split())
    start = int(input())

    graph = [[] for _ in range(v + 1)]
    distance = [INF] * (v + 1)
    for _ in range(e):
        a, b, dist = map(int, input().split())
        graph[a].append((b, dist))

    dijkstra(start)

    for i in range(1, v + 1):
        if distance[i] == INF:
            print("INF")
        else:
            print(distance[i])
