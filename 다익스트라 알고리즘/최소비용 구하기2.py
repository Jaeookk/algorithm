# 백준 11779 골드3
# 최소비용 구하기와 비교했을 때 "경로"를 추가적으로 구해야함


import sys
import heapq


def dijkstra(start, end):
    q = []
    # 우선순위 큐에 (최단 경로, 해당 노드, 해당노드 이전에 방문한 노드 리스트)를 추가하여
    # 경로 추적
    heapq.heappush(q, (0, start, []))

    INF = int(1e9)
    distance = [INF] * (n + 1)
    distance[start] = 0

    min_cost = INF

    while q:
        dist, now, stack = heapq.heappop(q)
        if dist > distance[now]:
            continue
        if now == end and min_cost > distance[now]:
            # 가장 최단 거리가 짧은 노드가 도착점과 같고, 그 거리가 이전 거리보다 짧다면
            min_cost = distance[now]  # min_cost 최신화
            result = stack + [end]  # 경로 최신화

        for next in graph[now]:
            cost = dist + next[1]
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(q, (cost, next[0], stack + [now]))

    return distance[end], result


if __name__ == "__main__":
    input = sys.stdin.readline

    n = int(input())
    m = int(input())

    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))

    start, end = map(int, input().split())

    cost, path = dijkstra(start, end)
    print(cost)
    print(len(path))
    print(*path)
