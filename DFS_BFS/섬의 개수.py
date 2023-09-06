import sys
from collections import deque


def bfs(y, x, graph, visited):
    dx = [0, 0, -1, 1, 1, 1, -1, -1]
    dy = [1, -1, 0, 0, 1, -1, 1, -1]
    q = deque()
    q.append((y, x))
    visited[y][x] = 1

    while q:
        cur_y, cur_x = q.popleft()
        for i in range(8):
            ny = cur_y + dy[i]
            nx = cur_x + dx[i]
            if 0 <= ny < h and 0 <= nx < w and graph[ny][nx] == 1:
                if not visited[ny][nx]:
                    visited[ny][nx] = 1
                    q.append((ny, nx))
    return 1


if __name__ == "__main__":
    input = sys.stdin.readline

    while True:
        w, h = map(int, input().split())
        if w == 0 and h == 0:
            break
        graph = []
        for _ in range(h):
            graph.append(list(map(int, input().split())))

        ret = 0
        visited = [[0 for _ in range(w)] for _ in range(h)]
        for r in range(h):
            for c in range(w):
                if graph[r][c] == 1 and not visited[r][c]:
                    ret += bfs(r, c, graph, visited)
        print(ret)
