# 백준 1240 골드5

from collections import deque
import sys


def bfs(start, end):
    q = deque([(start, 0)])
    visited = [0] * (n + 1)
    visited[start] = 1

    while q:
        cur, dis = q.popleft()  # 현재노드, start ~ 현재노드까지의 거리
        if cur == end:
            return dis

        for next, next_dis in graph[cur]:
            if not visited[next]:
                visited[next] = 1
                q.append((next, dis + next_dis))


if __name__ == "__main__":
    input = sys.stdin.readline

    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b, distance = map(int, input().split())
        graph[a].append((b, distance))
        graph[b].append((a, distance))

    for _ in range(m):
        a, b = map(int, input().split())
        print(bfs(a, b))
