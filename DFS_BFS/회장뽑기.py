# BOJ 2660 골드5
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
    return max(visited)


if __name__ == "__main__":
    n = int(input())
    graph = [[] for _ in range(n + 1)]
    while True:
        a, b = map(int, input().split())
        if a == -1 and b == -1:
            break
        graph[a].append(b)
        graph[b].append(a)

    score = 50
    lst = []

    for i in range(1, n + 1):
        tmp = bfs(i)
        if tmp < score:
            score = tmp
            lst = [i]
        elif tmp == score:
            lst.append(i)
    print(score, len(lst))
    print(*lst)
