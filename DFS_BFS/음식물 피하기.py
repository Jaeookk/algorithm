import sys
from collections import deque


def bfs(y, x, graph, visited):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    q = deque()
    q.append((y, x))
    visited[y][x] = 1
    count = 1

    while q:
        cur_y, cur_x = q.popleft()
        for i in range(4):
            ny = cur_y + dy[i]
            nx = cur_x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and graph[ny][nx] == 1:
                if not visited[ny][nx]:
                    visited[ny][nx] = 1
                    q.append((ny, nx))
                    count += 1
    return count


if __name__ == "__main__":
    input = sys.stdin.readline
    n, m, k = map(int, input().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        r, c = map(int, input().split())
        graph[r - 1][c - 1] = 1

    visited = [[0 for _ in range(m)] for _ in range(n)]
    ret = 0

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and not visited[i][j]:
                ret = max(ret, bfs(i, j, graph, visited))
    print(ret)
