# 백준 1238 골드3

import sys
import heapq


def dijkstra(start, graph):
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

    n, m, x = map(int, input().split())  # 노드, 간선 수, 도착지
    graph1 = [[] for _ in range(n + 1)]
    graph2 = [[] for _ in range(n + 1)]

    for _ in range(m):
        start, end, cost = map(int, input().split())
        graph1[start].append((end, cost))  # x에서 돌아오는 길
        graph2[end].append((start, cost))  # x로 가는 길

    # 양방향이 아닌데 start와 end를 바꿔서 graph에 저장해도 되는 이유?
    # 다익스트라에서 x를 시작점이라 가정했을 때, 문제에서 주어진 start ~ end를 그대로 활용하면 학생들이 x에서 다시 돌아가는 것으로 볼 수 있다.
    #
    # 그렇다면 다익스트라에서 x를 시작점으로 했을 때, x로 갈 때는 어떻게 해야 할까?
    # 만약 1 -> 3 -> x로 가는 최단거리 단방향 길이 있다고 하자.
    # x를 시작점으로 다익스트라를 돌렸을 때,  1->3->x로 이어지는 최단거리 단방향 길은 거꾸로 생각하여 x->3->1로 구할 수 있게 된다.
    # 그러므로 x로 가는 길을 구하기 위해서는 start와 end를 바꿔서 그래프에 저장하여 x를 출발점으로 하는 다익스트라를 돌리면, x까지 가는 각 마을에서의 최단 거리 리스트를 구할 수 있다.

    x_to_n = dijkstra(x, graph1)
    n_to_x = dijkstra(x, graph2)

    print(max(x_to_n[i] + n_to_x[i] for i in range(1, n + 1)))
