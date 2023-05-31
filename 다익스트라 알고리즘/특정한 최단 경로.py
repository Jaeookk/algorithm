# 백준 1504 골드4

import sys
import heapq


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))

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

    return distance


if __name__ == "__main__":
    input = sys.stdin.readline
    INF = int(1e9)

    n, e = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(e):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    x, y = map(int, input().split())  # 반드시 거쳐야 하는 정점

    # 출발점이 각각 1, x, y일 때의 최단 거리 배열
    start_with_1 = dijkstra(1)
    start_with_x = dijkstra(x)
    start_with_y = dijkstra(y)

    # 1 - x - y - n
    path1 = start_with_1[x] + start_with_x[y] + start_with_y[n]
    # 1 - y - x - n
    path2 = start_with_1[y] + start_with_y[x] + start_with_x[n]

    result = min(path1, path2)
    print(result if result < INF else -1)
