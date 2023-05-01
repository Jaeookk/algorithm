# BOJ 1325 실버1
import sys
from collections import deque


def bfs(x):
    queue = deque([x])
    count = 1
    visited = [0] * (n+1)
    visited[x] = 1

    while queue:
        x = queue.popleft()

        for i in graph[x]:
            if visited[i] == 0:
                visited[i] = 1
                queue.append(i)
                count += 1

    return count


if __name__ == "__main__":
    input = sys.stdin.readline
    
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for i in range(m):
        a,b = map(int,input().split())
        graph[b].append(a)

    maxResult = 1
    ans = []
    for i in range(1, n+1):
        cnt = bfs(i)
        if cnt > maxResult:
            maxResult = cnt
            ans = [i]
        elif cnt == maxResult:
            ans.append(i)
    
    print(*ans)